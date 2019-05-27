from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException, UnexpectedAlertPresentException, TimeoutException, NoSuchElementException
from Selenium.Configuration import BasePage


class Rewards(BasePage.BasePage):

    # element
    link_sign_in = (By.CSS_SELECTOR, "a[href*='signin']")

    # action
    def click_sign_in_link(self):
        self.wait.until(EC.element_to_be_clickable(Rewards.link_sign_in))
        sign_in_link = self.driver.find_elements(*Rewards.link_sign_in)
        sign_in_link[1].click()
