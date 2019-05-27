from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):

        self.accept_next_alert = True
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.verificationErrors = []
        self.base_url = None
