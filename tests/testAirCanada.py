import time
import pytest
from utils.browserSetup import get_browser

# This file will run the test to see if the website has loaded correctly

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

# This function initializes test function to be called during runtime
# Return: Driver - Returns driver setup from browserSetup.py and gets website URL
@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

# This function will test to see if the page title matches the desired string
# to ensure the correct page has loaded
def test_home_page_title(setup):
    driver = setup                                              # Call the setup fixture
    time.sleep(5)                                               # Wait 5 seconds for website to load
    assert 'Book Flights Online | Air Canada' in driver.title   # Assert Test Case