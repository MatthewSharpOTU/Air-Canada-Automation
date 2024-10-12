import time
import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By

# This file will run the test to see if the search flights feature from Toronto to Vancouver
# Departing Oct 30 and Returning Nov 02 functions as desired

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

# This function initializes test function to be called during runtime
# Return: Driver - Returns driver setup from browserSetup.py and gets website URL
@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

# This function will Input info into the desired text fields
# and assess to see if the next page in the planning the flights loaded
def test_search_flights_functionality(setup):
    # Setup Driver
    driver = setup
    # Wait for Page to Load
    time.sleep(5)

    # Locate and Click the Origin Location Button
    origin_location_input = driver.find_element(By.ID, "flightsOriginLocationbkmgLocationContainer")
    origin_location_input.click()

    # Locate the proper field and Input the desired Origin
    origin_location_input = driver.find_element(By.ID, "flightsOriginLocation")
    origin_location_input.send_keys("Toronto-Pearson Int.")
    time.sleep(1)

    # Locate and Click the Destination Location Button
    destination_location_input = driver.find_element(By.ID, "flightsOriginDestinationbkmgLocationContainer")
    destination_location_input.click()

    # Locate the proper field and Input the desired Destination
    destination_location_input = driver.find_element(By.ID, "flightsOriginDestination")
    destination_location_input.send_keys("Vancouver")
    time.sleep(1)

    # Locate the proper field and Input the desired Departure Date
    origin_date_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-1")
    origin_date_input.send_keys("30/10")
    time.sleep(1)

    # Locate the proper field and Input the desired Return Date
    destination_date_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-2")    
    destination_date_input.send_keys("02/11")
    time.sleep(1)

    # Locate the search button and Click it
    search_button = driver.find_element(By.XPATH, "//button[contains(@id, 'bkmg-desktop_findButton')][.//span[text()[contains(., ' Search ')]]]")
    search_button.click()

    # Wait for Flights to Load
    time.sleep(15)
    
    # Assert that flight results page appears
    departing = driver.find_element(By.XPATH, "//h1")
    assert "Departing flight" in departing.get_attribute('innerHTML')
