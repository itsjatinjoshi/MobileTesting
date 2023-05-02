import unittest

import pytest

from AppiumFramework.pages.EnterValuePage import EnterValueForm
import AppiumFramework.utilities.CustomerLogger as cl

from AppiumFramework.base.DriverClass import Driver
from AppiumFramework.pages.LoginPage import LoginPage

# driver1 = Driver().getDriverMethod()
#
# loginPage = LoginPage(driver1)
#
# loginPage.loginFormButton()
# loginPage.loginPageTitle()
# loginPage.loginPageEmail()
# loginPage.loginPagePswd()
# loginPage.loginSubmitButton()
#
# loginPage.adminPageTitle()
# loginPage.adminPageTextField()
# loginPage.adminPageSubmitButton()
# loginPage.adminPagePreview()

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class LoginPageTest(unittest.TestCase):
    logger = cl.customLogger()

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.loginPage = LoginPage(self.driver)

    @pytest.mark.run(order=6)
    def test_open_login_value_form(self):
        self.loginPage.loginPageEmail()
        self.loginPage.loginPagePswd()
        self.loginPage.loginSubmitButton()

        self.loginPage.adminPageTitle()
        self.loginPage.adminPageTextField()
        self.loginPage.adminPageSubmitButton()
        # self.loginPage.adminPagePreview()

    @pytest.mark.run(order=5)
    def test_enter_login_value_form(self):
        self.loginPage.loginFormButton()
        self.loginPage.loginPageTitle()
