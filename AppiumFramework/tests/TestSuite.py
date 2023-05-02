import unittest

from AppiumFramework.tests.LoginFormTest import LoginPageTest
from AppiumFramework.tests.ContactUsFormTest import ContactUsFormTest
from AppiumFramework.tests.EnterValuePageTest import EnterValuePageTest
from AppiumFramework.tests.ScrollViewTest import ScrollViewTest

login_page = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
contact_us_page = unittest.TestLoader().loadTestsFromTestCase(ContactUsFormTest)
enter_value_page = unittest.TestLoader().loadTestsFromTestCase(EnterValuePageTest)
scroll_view_page = unittest.TestLoader().loadTestsFromTestCase(ScrollViewTest)

regression_test = unittest.TestSuite([login_page, contact_us_page,
                                      enter_value_page, scroll_view_page])

unittest.TextTestRunner(verbosity=1).run(regression_test)
