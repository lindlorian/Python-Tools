import unittest
from Selenium.Support.UrlSupport import UrlConstants
from Selenium.Configuration import WebdriverConfiguration
from Selenium.Pages import Rewards, SignIn


class TestStarbucks(unittest.TestCase):

    def setUp(self):

        self.driver = None
        webdriver_config = WebdriverConfiguration.WebdriverConfiguration(self.driver)
        self.driver = webdriver_config.set_driver(browser="chrome", enable_listener=True)
        self.base_url = UrlConstants.URL_STARBUCKS_REWARDS
        self.driver.get(self.base_url)

    def _test_has_failed(self):

        for method, error in self._outcome.errors:
            if error:
                return True
        return False

    def tearDown(self):
        self.driver.quit()

    def test_sign_in_from_rewards_page_fails(self):
        rewards_page = Rewards.Rewards(self.driver)
        rewards_page.click_sign_in_link()
        sign_in_page = SignIn.SignIn(self.driver)
        sign_in_page.set_username(auto_select=True, username="")
        sign_in_page.set_password(auto_select=True, pwd="")
        sign_in_page.click_sign_in_link()
        sign_in_page.assert_sign_in_failed()


