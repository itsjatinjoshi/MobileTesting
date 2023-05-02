import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, \
    ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Google Pixel 3 XL'
desired_caps['app'] = 'C:\\Users\\Jatin-PC\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 45, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# text_view = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.TextView")
# text_view = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ContactUs")
# text_view.click()

t = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ContactUs"))
print(t)
t.click()

# time.sleep(3)
# driver.quit()
