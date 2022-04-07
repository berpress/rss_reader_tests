from selenium.webdriver.common.by import By


class MainPage:
    INPUT = (By.ID, "input")
    SUBMIT = (By.ID, "submit")
    ERROR_TEXT = (By.CSS_SELECTOR, ".feedback")

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        """
        open main page
        """
        self.app.driver.get(self.app.url)

    def add_css_url(self, url: str):
        """
        Add css url on main page
        :param url: url
        """
        input_field = self.app.driver.find_element(*self.INPUT)
        input_field.send_keys(url)
        start_button = self.app.driver.find_element(*self.SUBMIT)
        start_button.click()

    def error_text(self) -> str:
        element = self.app.driver.find_element(*self.ERROR_TEXT)
        return element.text
