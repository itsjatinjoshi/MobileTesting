import time
import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException, \
    ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFramework.utilities.CustomerLogger as cl


class BaseTest():
    logger = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 45, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID,
                                                          locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,
                                                          locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(lambda x: x.find_element(AppiumBy.
                                                          ANDROID_UIAUTOMATOR,
                                                          'UiSelector().description("%s")' % (
                                                              locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(lambda x: x.find_element(AppiumBy.
                                                          ANDROID_UIAUTOMATOR,
                                                          'UiSelector().description("%d")' % int(
                                                              locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy
                                                          .ANDROID_UIAUTOMATOR,
                                                          'text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.XPATH, 's' % (locatorValue)))
            return element
        else:
            self.logger.info("Locator value " + locatorValue + " Not found.")
        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:

            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.logger.info(
                f"Element found with LocatorType {locatorType} and"
                f" LocatorValue {locatorValue}")
        except:
            self.logger.info(
                f"Element not found with LocatorType {locatorType}"
                f" and LocatorValue {locatorValue}")
        return element

    def getClick(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.logger.debug(
                f"Click on element with LocatorType {locatorType}"
                f" and LocatorValue {locatorValue}")
        except:
            self.logger.info(f"Unable to click Element with LocatorType "
                             f"{locatorType} and LocatorValue {locatorValue}")

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.logger.info(
                f"Send text on element with LocatorType {locatorType}"
                f" and LocatorValue {locatorValue}")
        except:
            self.logger.info(f"Unable to send text element with LocatorType "
                             f"{locatorType} and LocatorValue {locatorValue}")
            self.getScreenshot(locatorType)
            assert False

    def getText(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element = element.get_attribute(locatorType)
            self.logger.info(
                f"Get text on element with LocatorType {locatorType}"
                f" and LocatorValue {locatorValue}")
            return element
        except:
            self.logger.info(f"Unable to get text element with LocatorType "
                             f"{locatorType} and LocatorValue {locatorValue}")
            self.getScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.logger.debug(f"Element is Displayed with LocatorType "
                              f"{locatorType} and LocatorValue {locatorValue}")
            return True
        except:
            self.logger.debug(f"Element is not present with LocatorType "
                              f"{locatorType} and LocatorValue {locatorValue}")
            return False

    def scrollView(self, text):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                 NoSuchElementException])
        wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'new UiScrollable(new UiSelector()).scrollIntoView(text("{text}"))'))

    def getScreenshot(self, screenshotName):
        time_stamp = time.strftime("%d_%m_%y_%H_%M_%S")
        fileName = f'{screenshotName}_{time_stamp}.png'
        screenshotDir = "../screenshots/"
        screenshotPath = screenshotDir + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.logger.info(f"Screenshot saved to the path: {screenshotPath}")
        except:
            self.logger.info(
                f"Screenshot not saved to the path: {screenshotPath}",
                )

    def getScreenshot(self, file_name):
        allure.attach(self.driver.get_screenshot_as_png(), name=file_name,
                      attachment_type=AttachmentType.PNG)
