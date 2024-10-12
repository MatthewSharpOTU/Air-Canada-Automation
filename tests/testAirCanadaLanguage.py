import time
import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By

# This file will run the test to see if the website language will change to French

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

# This function initializes test function to be called during runtime
# Return: Driver - Returns driver setup from browserSetup.py and gets website URL
@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

# This Function will load perform clicks on desired elements to change the page
# from English to French
def test_language_change_to_french(setup):
    # Call Setup Fixture
    driver = setup
    # Wait 5 Seconds for Website to Load
    time.sleep(5)

    # Locate and click the language selector
    language_button = driver.find_element(By.XPATH, "//button[contains(@id, 'acSiteEditionSelectorDesktop-button')][.//div[contains(@class, 'ngx-ac-site-edition-selector-content')]][.//span[text()[contains(., 'EN')]]]")
    language_button.click()

    # Wait 1 Second for Elements to Be Present
    time.sleep(1)
    
    # Locate and Click the Current Language (English)
    language_button = driver.find_element(By.XPATH, "//div[text()[contains(., 'English')]]")
    language_button.click()

    # Wait 1 Second for Dropdown Elements to Be Present
    time.sleep(1)

    # Locate and Click the Desired Language in the Dropdown
    language_button = driver.find_element(By.XPATH, "//div[contains(@id, 'siteLanguageDropdownOptionsPanel')][.//div[text()[contains(., 'Français')]]]")
    language_button.click()

    # Locate and Click the Confirm Button for this Div
    language_button = driver.find_element(By.XPATH, "//button[contains(@id, 'acEditionSelectorConfirmButton')][.//span[text()[contains(., ' Confirm ')]]]")
    language_button.click()

    # Wait for Website to Load
    time.sleep(5)

    # Assert Test Case to verify if page switched to French
    assert "Réservation de vols en ligne | Air Canada" in driver.title