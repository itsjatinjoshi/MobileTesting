from AppiumFramework.base.BaseTest import BaseTest
import AppiumFramework.utilities.CustomerLogger as cl


class EnterValueForm(BaseTest):
    logger = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _enter_value_btn = "com.code2lead.kwad:id/EnterValue"  # id
    _enter_value_title = "Enter some Value"  # text
    _enter_value_text_field = "com.code2lead.kwad:id/Et1"  # id
    _enter_value_submit_btn = "com.code2lead.kwad:id/Btn1"  # id

    def enterValueButton(self):
        self.getClick(self._enter_value_btn, "id")
        self.logger.info("ENTER VALUE BUTTON CLICKED.")

    def enterValueTitle(self):
        title = self.isDisplayed(self._enter_value_title, "text")
        assert title, "Wrong title found."
        self.logger.info("VERIFY ENTER VALUE PAGE.")

    def enterValueTextField(self):
        self.sendText("Hello All", self._enter_value_text_field, "id")
        self.logger.info("ENTER TEXT IN TEXT FIELD.")

    def enterValueSubmitBtn(self):
        self.getClick(self._enter_value_submit_btn, "id")
        self.logger.info("SUBMIT BUTTON CLICKED.")

