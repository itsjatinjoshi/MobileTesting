import unittest

import pytest

from AppiumFramework.base.DriverClass import Driver
from AppiumFramework.pages.ScrollViewPage import ScrollViewPage


# drive1 = Driver()
# d =drive1.getDriverMethod()
#
# scrollView = ScrollViewPage(d)
#
# scrollView.clickOnScrollFormButton()
# scrollView.verifyScrollViewPage()
# scrollView.scrollViewBtnClickedAndPressNo()
# scrollView.scrollViewBtnClickedAndPressYes()

@pytest.mark.usefixtures("class_fixture", "method_fixture")
class ScrollViewTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.scrollView = ScrollViewPage(self.driver)

    @pytest.mark.run(order=8)
    def test_open_scroll_view_form(self):
        self.scrollView.scrollViewBtnClickedAndPressNo()
        self.scrollView.scrollViewBtnClickedAndPressYes()

    @pytest.mark.run(order=7)
    def test_scroll_view_form(self):
        self.scrollView.clickOnScrollFormButton()
        self.scrollView.verifyScrollViewPage()
