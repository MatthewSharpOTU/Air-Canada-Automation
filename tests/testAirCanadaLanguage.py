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

def test_language_change_to_french(setup):
    driver = setup
    
    time.sleep(5)

    # Locate and click the language selector
    language_button = driver.find_element(By.XPATH, "//button[contains(@id, 'acSiteEditionSelectorDesktop-button')][.//div[contains(@class, 'ngx-ac-site-edition-selector-content')]][.//span[text()[contains(., 'EN')]]]")
    # language_button = driver.find_element(By.XPATH, "//button[@lang='fr']")
    language_button.click()

    time.sleep(1)
    
    language_button = driver.find_element(By.XPATH, "//div[text()[contains(., 'English')]]")
    language_button.click()

    time.sleep(1)

    language_button = driver.find_element(By.XPATH, "//div[contains(@id, 'siteLanguageDropdownOptionsPanel')][.//div[text()[contains(., 'Français')]]]")
    language_button.click()

    time.sleep(1)

    language_button = driver.find_element(By.XPATH, "//button[contains(@id, 'acEditionSelectorConfirmButton')][.//span[text()[contains(., ' Confirm ')]]]")
    language_button.click()

    time.sleep(5)

    # Verify if page switched to French
    assert "Réservation de vols en ligne | Air Canada" in driver.title