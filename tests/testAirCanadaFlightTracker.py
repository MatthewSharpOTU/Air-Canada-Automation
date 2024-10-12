import time
import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

def test_flight_tracker_page_access(setup):
    driver = setup
    
    time.sleep(5)

    flight_status = driver.find_element(By.ID, "nav-button-12")
    flight_status.click()

    time.sleep(1)

    flight_number = driver.find_element(By.ID, "abcFormFieldElement64")
    flight_number.send_keys("181")

    time.sleep(1)


    flight_date = driver.find_element(By.XPATH, "//div[contains(@class, 'abc-form-element-infix')][.//div[contains(@class, 'abc-selected-option-text')]]")
    flight_date.click()

    time.sleep(2)

    flight_departure = driver.find_element(By.XPATH, "//div[text()[contains(., 'Tue Oct 15')]]")

    try:
            # Attempt to click on the element
            flight_departure.click()
    except ElementClickInterceptedException:
            # If click is intercepted, perform a JavaScript click
            print("Element click was intercepted")
            driver.execute_script("arguments[0].click();", flight_departure)

    
    time.sleep(1)

    search_button = driver.find_element(By.ID, "abcButtonElement67")
    search_button.click()

    time.sleep(5)

    assert "AC 181 on Oct 15 - Flight Status - Air Canada" in driver.title