from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

def test_home_page_title(setup):
    driver = setup
    time.sleep(5)
    assert 'Book Flights Online | Air Canada' in driver.title
