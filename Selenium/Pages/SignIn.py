from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Selenium.Configuration import BasePage


class SignIn(BasePage.BasePage):

    # element
    button_sign_in = (By.XPATH, "//button[@data-e2e='signInButton']")
    div_sign_in_failed = (By.CSS_SELECTOR, "div[class*='alert']")
    input_password = (By.ID, 'password')
    input_username = (By.ID, 'username')

    # action
    def assert_sign_in_failed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(SignIn.div_sign_in_failed))
        except TimeoutException:
            raise Exception("Expected Behavior: Sign In Failed Element Visible\nActual: Element not visible.")

    def click_sign_in_link(self):
        self.wait.until(EC.element_to_be_clickable(SignIn.button_sign_in))
        sign_in_link = self.driver.find_element(*SignIn.button_sign_in)
        sign_in_link.click()
        self.wait.until_not(EC.visibility_of_element_located(SignIn.button_sign_in))

    def set_username(self, auto_select=True, username=""):
        if auto_select is True:
            username = "example@example.com"
        actions = ActionChains(self.driver)
        username_input = self.driver.find_element(*SignIn.input_username)
        username_input.click()
        self.wait.until(EC.element_to_be_clickable(SignIn.input_username))
        actions.send_keys_to_element(username_input, username)
        actions.perform()
        return username

    def set_password(self, auto_select=True, pwd=""):
        if auto_select is True:
            pwd = "Testing"
        actions = ActionChains(self.driver)
        pwd_input = self.driver.find_element(*SignIn.input_password)
        pwd_input.click()
        self.wait.until(EC.element_to_be_clickable(SignIn.input_password))
        actions.send_keys_to_element(pwd_input, pwd)
        actions.perform()
        return pwd
