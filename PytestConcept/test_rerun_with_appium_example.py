import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import allure

@pytest.mark.flaky(reruns=5)
def test_run_with_appium():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Google Pixel 3 XL'
    desired_caps['app'] = 'C:\\Users\\Jatin-PC\\Downloads\\Android_Demo_App.apk'
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    enterValue = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValu")
    enterValue.click()

    time.sleep(3)
    driver.quit()
