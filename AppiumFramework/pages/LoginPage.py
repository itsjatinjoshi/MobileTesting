import time

from AppiumFramework.base.BaseTest import BaseTest
import AppiumFramework.utilities.CustomerLogger as cl


class LoginPage(BaseTest):
    logger = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Login Page
    _loginPageForm = "com.code2lead.kwad:id/Login"  # id
    _loginPageTitle = "Login Page"  # text
    _loginPageEmail = "com.code2lead.kwad:id/Et4"  # id
    _loginPagePswd = "com.code2lead.kwad:id/Et5"  # id
    _loginButton = "LOGIN"  # text

    # Admin Page
    _adminPageTitle = "Enter Admin"  # text
    _adminPageTextField = "com.code2lead.kwad:id/Edt_admin"  # id
    _adminPageSubmitButton = "SUBMIT"  # text
    _adminPagePreview = "com.code2lead.kwad:id/Tv_admin"  # id

    def loginFormButton(self):
        self.getClick(self._loginPageForm, "id")

    def loginPageTitle(self):
        login_title = self.isDisplayed(self._loginPageTitle,
                                       "text")
        assert login_title, "Wrong title found."

    def loginPageEmail(self):
        self.sendText("admin@gmail.com", self._loginPageEmail, "id")

    def loginPagePswd(self):
        self.sendText("admin123", self._loginPagePswd, "id")

    def loginSubmitButton(self):
        self.getClick(self._loginButton, "text")

    def adminPageTitle(self):
        login_title = self.isDisplayed(self._adminPageTitle,
                                       "text")
        assert login_title, "Wrong title found."

    def adminPageTextField(self):
        self.sendText("admin@gmail.com", self._adminPageTextField, "id")

    def adminPageSubmitButton(self):
        self.getClick(self._adminPageSubmitButton, "text")

    # todo : need to reterive the result and comapre it with input.
    #  Make sure if its print same output
    # def adminPagePreview(self):
    #     time.sleep(5)
    #     get_text = self.getText(self._adminPagePreview, "id")
    #     self.logger.info(get_text)
    #     assert get_text == "admin@gmail.com", "Value not matched."
