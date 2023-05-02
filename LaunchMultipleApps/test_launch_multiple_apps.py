import time

from appium import webdriver

def test_launch_multiple_apps():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '11'
    desired_caps['deviceName'] = 'Google Pixel 3 XL'
    desired_caps['app'] = 'C:\\Users\\Jatin-PC\\Downloads\\Android_Demo_App.apk'
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    time.sleep(5)
    driver.start_activity("com.android.documentsui", "com.android.documentsui.files.FilesActivity")

    time.sleep(5)
    driver.start_activity("com.code2lead.kwad", "com.code2lead.kwad.MainActivity")
    time.sleep(5)
    driver.quit()
