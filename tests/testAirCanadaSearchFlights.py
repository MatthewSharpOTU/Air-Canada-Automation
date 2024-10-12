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

def test_search_flights_functionality(setup):
    driver = setup
    time.sleep(7)
    # Find the "Book" section and enter a route

    origin_location_input = driver.find_element(By.ID, "flightsOriginLocationbkmgLocationContainer")
    origin_location_input.click()
    time.sleep(1)

    origin_location_input = driver.find_element(By.ID, "flightsOriginLocation")
    origin_location_input.send_keys("Toronto-Pearson Int.")
    time.sleep(1)

    destination_location_input = driver.find_element(By.ID, "flightsOriginDestinationbkmgLocationContainer")
    destination_location_input.click()
    time.sleep(1)

    destination_location_input = driver.find_element(By.ID, "flightsOriginDestination")
    destination_location_input.send_keys("Vancouver")
    time.sleep(1)

    origin_date_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-1")
    destination_date_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-2")

    origin_date_input.send_keys("30/10")
    time.sleep(1)
    destination_date_input.send_keys("02/11")
    time.sleep(1)

    # # Find the search button and click it
    search_button = driver.find_element(By.XPATH, "//button[contains(@id, 'bkmg-desktop_findButton')][.//span[text()[contains(., ' Search ')]]]")
    search_button.click()

    time.sleep(15)
    
    # # Assert that flight results page appears
    departing = driver.find_element(By.XPATH, "//h1")
    assert "Departing flight" in departing.get_attribute('innerHTML')
