import logging

import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.app import Application

logger = logging.getLogger("rss")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://rss-litovsky.vercel.app/",
        help="RSS url",
    ),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    app = Application(driver, url)
    yield app
    app.quit()
