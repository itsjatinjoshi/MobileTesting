import unittest

import pytest

from AppiumFramework.pages.EnterValuePage import EnterValueForm
from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utilities.CustomerLogger as cl


# class EnterValuePageTest():
#     driver = Driver()
#     enterValues = EnterValueForm(driver.getDriverMethod())
#     enterValues.enterValueButton()
#     enterValues.enterValueTitle()
#     enterValues.enterValueTextField()
#     enterValues.enterValueSubmitBtn()

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class EnterValuePageTest(unittest.TestCase):
    logger = cl.customLogger()

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.enterValues = EnterValueForm(self.driver)

    @pytest.mark.run(order=3)
    def test_open_enter_value_form(self):
        self.enterValues.enterValueButton()
        self.enterValues.enterValueTitle()

    @pytest.mark.run(order=4)
    def test_enter_value_form(self):
        self.enterValues.enterValueTextField()
        self.enterValues.enterValueSubmitBtn()


