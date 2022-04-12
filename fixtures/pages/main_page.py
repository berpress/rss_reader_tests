from selenium.webdriver.common.by import By

from fixtures.pages.base_page import BasePage


class MainPage(BasePage):
    INPUT = (By.ID, "input")
    SUBMIT = (By.ID, "submit")
    ERROR_TEXT = (By.CSS_SELECTOR, ".feedback")

    def open_main_page(self):
        """
        open main page
        """
        self.open_page(self.app.url)

    def add_css_url(self, url: str):
        """
        Add css url on main page
        :param url: url
        """
        self.fill(locator=self.INPUT, value=url)
        self.click(locator=self.SUBMIT)

    def error_text(self) -> str:
        return self.text(locator=self.ERROR_TEXT)
