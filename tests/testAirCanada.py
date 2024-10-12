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

# def test_home_page_title(setup):
#     driver = setup
#     time.sleep(5)
#     page_title = driver.find_element(By.XPATH, "//h1[contains(@class, 'ac-page-title')]")
#     assert ' Where can we take you? ' in page_title.get_attribute("innerHTML")

# def test_search_flights_functionality(setup):
#     driver = setup
#     time.sleep(5)
#     # Find the "Book" section and enter a route

#     # origin_input = driver.find_element(By.ID, "flightsOriginLocation")
#     # destination_input = driver.find_element(By.ID, "flightsOriginDestination")

#     origin_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-1")
#     destination_input = driver.find_element(By.ID, "bkmg-desktop_travelDates-formfield-2")

#     origin_input.send_keys("30/10")
#     time.sleep(1)
#     destination_input.send_keys("02/11")
#     time.sleep(1)

#     # # Find the search button and click it
#     search_button = driver.find_element("By.XPATH", "//div[contains(@class, 'find-btn')][.//span[text()[contains(., ' Search ')]]]")
#     time.sleep(1)
#     search_button.click()

#     time.sleep(3)
    
#     # # Assert that flight results page appears
#     assert "flights" in driver.current_url.lower()
#     driver.quit()

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

# def test_contact_us_page_access(setup):
#     driver = setup
    
#     # Scroll to the bottom of the page to find "Contact Us"
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     time.sleep(2)

#     contact_us_link = driver.find_element(By.LINK_TEXT, "Contact Us")
#     contact_us_link.click()

#     time.sleep(3)
    
#     # Verify if "Contact Us" page loaded
#     assert "contact-us" in driver.current_url
