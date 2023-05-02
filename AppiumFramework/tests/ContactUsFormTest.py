import unittest
import pytest
from AppiumFramework.pages.ContactUsFormPage import ContactUsForm
import AppiumFramework.utilities.CustomerLogger as cl

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class ContactUsFormTest(unittest.TestCase):
    logger = cl.customLogger()

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.contactForm = ContactUsForm(self.driver)

    @pytest.mark.run(order=1)
    def test_open_contact_us_form(self):
        self.logger.info("APP LAUNCHED.")
        self.contactForm.clickContactFormButton()
        self.contactForm.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_contact_us_form(self):
        self.contactForm.contactPageName()
        self.contactForm.contactPageEmail()
        self.contactForm.contactPageAddress()
        self.contactForm.contactPageMobileNum()
        self.contactForm.contactPageSubmitBtn()
