from fixtures.pages.main_page import MainPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.main_page = MainPage(self)

    def quit(self):
        self.driver.quit()
