from appium import webdriver


class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'Google Pixel 3 XL'
        desired_caps['app'] = 'C:\\Users\\Jatin-PC\\Downloads\\Android_Demo_App.apk' # noqa
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
