import time
import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# This file will run the test to see if the flight tracker page will load
# It will then enter a flight number for Tuesday October 15 and search to find the status of the flight

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

# This function initializes test function to be called during runtime
# Return: Driver - Returns driver setup from browserSetup.py and gets website URL
@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

# This Function will traverse to the Flight Tracker, input
# The desired information and then check to see if we are brought to the flight's page
def test_flight_tracker_page_access(setup):
    # Setup Driver
    driver = setup
    # Wait for Webpage to Load
    time.sleep(5)

    # Locate and Click the button for the Flight Tracker
    flight_status = driver.find_element(By.ID, "nav-button-12")
    flight_status.click()

    # Wait for page to reload
    time.sleep(1)

    # Locate and Find the Input Field for the Flight Number
    flight_number = driver.find_element(By.ID, "abcFormFieldElement64")
    # Depending on When This is being tested you may have to change the below flight number and dates
    flight_number.send_keys("181") 

    # Locate and Click the Dropdown Menu for the Date Selector
    flight_date = driver.find_element(By.XPATH, "//div[contains(@class, 'abc-form-element-infix')][.//div[contains(@class, 'abc-selected-option-text')]]")
    flight_date.click()

    # Wait for Dropdown to Appear
    time.sleep(1)

    # Find the element with the desired flight day
    # May need to Change this Date
    flight_departure = driver.find_element(By.XPATH, "//div[text()[contains(., 'Tue Oct 15')]]")

    try:
            # Attempt to click on the element
            flight_departure.click()
    except ElementClickInterceptedException:
            # If click is intercepted, perform a JavaScript click instead
            print("Element click was intercepted")
            driver.execute_script("arguments[0].click();", flight_departure)

    # Locate and Click the Search Button
    search_button = driver.find_element(By.ID, "abcButtonElement67")
    search_button.click()

    # Wait for Page to Load
    time.sleep(5)

    # Assert the title of window the verify we are looking at this flights given status
    assert "AC 181 on Oct 15 - Flight Status - Air Canada" in driver.title