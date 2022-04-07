from fixtures.constants import ErrorText


class TestCSSPage:
    def test_add_valid_url(self, app):
        """
        1. Open main page
        2. Add valid url
        3. Check result text
        """
        app.main_page.open_main_page()
        app.main_page.add_css_url(url='https://lenta.ru/rss/news')
        assert app.main_page.error_text() == ErrorText.ERROR_NETWORK

    def test_add_invalid_url(self, app):
        """
        1. Open main page
        2. Add invalid url
        3. Check result text
        """
        app.main_page.open_main_page()
        app.main_page.add_css_url(url='test')
        assert app.main_page.error_text() == ErrorText.ERROR_INVALID
