from AppiumFramework.base.BaseTest import BaseTest
import AppiumFramework.utilities.CustomerLogger as cl


class ScrollViewPage(BaseTest):
    logger = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _scrollPageFormBtn = "com.code2lead.kwad:id/ScrollView"  # id
    _scrollPageTitle = "ScrollView"  # text
    _scrollPageBtn = "BUTTON"  # text
    _alterPopUp = "com.code2lead.kwad:id/title_template"  # id
    _alertPopUpYes = "YES"  # text
    _alertPopUpNo = "NO"  # text

    def clickOnScrollFormButton(self):
        self.getClick(self._scrollPageFormBtn, "id")
        self.logger.info("SCROLL VIEW BUTTON CLICKED.")

    def verifyScrollViewPage(self):
        title = self.isDisplayed(self._scrollPageTitle, "text")
        assert title, f"{title} Page not Found"

    def _verifyPopUpWindow(self):
        popUpWindow = self.isDisplayed(self._alterPopUp, "id")
        assert popUpWindow, "Pop Up Window Not Found."

    def _clickOnNo(self):
        self.getClick(self._alertPopUpNo, "text")

    def _clickOnYes(self):
        self.getClick(self._alertPopUpYes, "text")
        self.clickOnScrollFormButton()

    def scrollViewBtnClickedAndPressNo(self):
        # todo: change the range to all the list of buttons
        # todo: need to find the solution for it
        for i in range(0, 15):
            self.logger.info(self._scrollPageBtn+str(i+1))
            self.scrollView(self._scrollPageBtn+str(i+1))
            self.getClick(self._scrollPageBtn+str(i+1), "text")
            self._verifyPopUpWindow()
            self._clickOnNo()

    def scrollViewBtnClickedAndPressYes(self):
        for i in range(0, 15):
            self.scrollView(self._scrollPageBtn + str(i + 1))
            self.getClick(self._scrollPageBtn+str(i+1), "text")
            self._verifyPopUpWindow()
            self._clickOnYes()



