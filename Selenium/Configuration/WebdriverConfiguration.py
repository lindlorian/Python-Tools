from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver
from Selenium.Configuration import EventListener
from Selenium.Configuration import BasePage


class WebdriverConfiguration(BasePage.BasePage):

    def configure_chromedriver_with_event_listener(self):

        options = Options()

        if platform == "darwin":

            browser = webdriver.Chrome(chrome_options=options)

        else:

            browser = webdriver.Chrome("C:\\path\\to\\chromedriver.exe", chrome_options=options)

        self.driver = EventFiringWebDriver(browser, EventListener.EventListener())

        return self.driver

    def set_driver(self, browser="", enable_listener=True):

        """Configure the appropriate webdriver by entering the name of the corresponding browser"""

        if browser == "chrome":

            if enable_listener is True:
                self.configure_chromedriver_with_event_listener()

            else:
                self.driver = webdriver.Chrome()

        return self.driver

