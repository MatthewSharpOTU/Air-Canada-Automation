import pytest
from utils.browser_setup import get_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_home_page_title(setup):
    driver = setup
    assert "Air Canada" in driver.title

def test_search_flights_functionality(setup):
    driver = setup
    
    # Find the "Book" section and enter a route
    origin_input = driver.find_element(By.ID, "origin_R_1")
    destination_input = driver.find_element(By.ID, "destination_R_1")

    origin_input.send_keys("Toronto")
    time.sleep(1)
    destination_input.send_keys("Vancouver")
    time.sleep(1)

    # Find the search button and click it
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Find flights')]")
    search_button.click()

    time.sleep(3)
    
    # Assert that flight results page appears
    assert "flights" in driver.current_url.lower()

def test_language_change_to_french(setup):
    driver = setup
    
    # Locate and click the language selector
    language_button = driver.find_element(By.XPATH, "//button[@lang='fr']")
    language_button.click()

    time.sleep(2)
    
    # Verify if page switched to French
    assert "Air Canada - Site officiel" in driver.title

def test_contact_us_page_access(setup):
    driver = setup
    
    # Scroll to the bottom of the page to find "Contact Us"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(2)

    contact_us_link = driver.find_element(By.LINK_TEXT, "Contact Us")
    contact_us_link.click()

    time.sleep(3)
    
    # Verify if "Contact Us" page loaded
    assert "contact-us" in driver.current_url
