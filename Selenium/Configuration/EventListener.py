from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.events import AbstractEventListener
from selenium.common.exceptions import StaleElementReferenceException


class EventListener(AbstractEventListener):

    def before_click(self, element, driver):
        value = element.text
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.perform()
        driver.save_screenshot("%s.png" % value)

    def on_exception(self, exception, driver):
        if exception == StaleElementReferenceException:
            pass
