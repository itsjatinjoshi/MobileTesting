from appium import webdriver
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
1.) Mobile Browser version and ChromeDriver or respective Browser Driver should be in same version 
2.) 
Two Ways of Identifying locators on webview i) open chrome browser and type "chrome://inspect/#devices" ii) Use Browser 
inspectors 

"""
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '10'
# desired_caps['deviceName'] = 'Pixel 3 XL'
# desired_caps['app'] = ('C:/Users/Jatin-PC/Downloads/Android_Demo_App.apk')
# desired_caps['appPackage'] = 'com.android.chrome'
# desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Google Pixel 3 XL'
desired_caps['app'] = 'C:\\Users\\Jatin-PC\\Downloads\\Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

# 1. Create the Driver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 2. Create WebDriverWait
wait = WebDriverWait(driver, 45, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# 3. Open the URL in Browser
accept_and_cont = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept"))
accept_and_cont.click()

navigate_button = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button"))
navigate_button.click()

search_box = wait.until(lambda  x: x.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text"))
search_box.click()

url_box = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
url_box.click()
url_box.send_keys("https://www.google.com/")
driver.press_keycode(66)

# 4. Get the list of Contexts in App
appContexts = driver.contexts
print("AppContexts : ", appContexts)

# # 5. switch to webview to perform action on Required URL or on WebView
# for appType in appContexts:
#     if appType == "WEBVIEW_chrome":
#         driver.switch_to.context(appType)
#
# # 6. Do testing on Webview screen in chrome browser or any if we want
# ele4 = wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//*[@name='q']"))
# ele4.send_keys("Skill2Lead")
#
# # 7. Switch back to native view to perform action
# for appType in appContexts:
#     if appType == "NATIVE_APP":
#         driver.switch_to.context(appType)
#
# # 8. Do testing on native app screen if we want
#
# ele4 = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar"))
# ele4.click()
# ele4.send_keys("https://www.skill2lead.com/")
# driver.press_keycode(66)

# 9. Quit or close the driver object

time.sleep(5)
driver.quit()
