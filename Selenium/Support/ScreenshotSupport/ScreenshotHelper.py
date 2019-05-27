
class ScreenshotHelper:

    def screenshot_bottom_of_page(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.get_screenshot_as_file("%s_bottom.png" % screenshot_name)

    def escape_chars(self, text):
        esc_chars = "@'[]"
        convert_chars = "/="
        for char in esc_chars:
            if char in text:
                text = text.replace(char, "")
        for char in convert_chars:
            if char in text:
                text = text.replace(char, "_")
        return text


    def set_screenshot_name(self, driver, value):
        current_url = self.find_current_url(driver)
        driver.get_screenshot_as_file("%s_bottom.png" % screenshot_name)
        driver.execute_script("scroll(0, 0);")

    def get_current_url(self):
        current_url = self.find_current_url(driver)
        return current_url