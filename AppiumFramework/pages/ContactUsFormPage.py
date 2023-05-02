from AppiumFramework.base.BaseTest import BaseTest
import AppiumFramework.utilities.CustomerLogger as cl


class ContactUsForm(BaseTest):
    logger = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _contactUsForm = "com.code2lead.kwad:id/ContactUs"  # id
    _contactUsPageTitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNum = "Enter Mobile No"  # text
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.getClick(self._contactUsForm, "id")
        self.logger.info("CONTACT US BUTTON CLICKED.")

    def verifyContactPage(self):
        title = self.isDisplayed(self._contactUsPageTitle, "text")
        assert title == True, "Wrong Title has found."
        self.logger.info("VERIFY CONTACT PAGE.")

    def contactPageName(self):
        self.sendText("ABC", self._enterName, "text")
        self.logger.info("CONTACT PAGE NAME.")

    def contactPageEmail(self):
        self.sendText("ahaha@email.com", self._enterEmail, "text")
        self.logger.info("CONTACT PAGE EMAIL.")

    def contactPageAddress(self):
        self.sendText("USA", self._enterAddress, "text")
        self.logger.info("CONTACT PAGE ADDRESS.")

    def contactPageMobileNum(self):
        self.sendText("12321232", self._enterMobileNum, "text")
        self.logger.info("CONTACT PAGE MOBILE NUMBER.")

    def contactPageSubmitBtn(self):
        self.getClick(self._submitButton, "text")
        self.logger.info("CONTACT PAGE SUBMIT BUTTON.")
