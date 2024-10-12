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

def test_contact_us_page_access(setup):
    driver = setup
    
    time.sleep(5)

    # Scroll to the bottom of the page to find "Contact Us"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(3)

    contact_us_link = driver.find_element(By.LINK_TEXT, "Help And Contact")
    contact_us_link.click()

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)

    page_traversal = driver.find_element(By.XPATH, "//a[text()[contains(., 'View all')]]")
    page_traversal.click()

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 250);")

    time.sleep(2)

    page_traversal = driver.find_element(By.XPATH, "//a[text()[contains(., 'Carry-on baggage')]]")
    page_traversal.click()

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[2])

    time.sleep(3)

    liquids_tab = driver.find_element(By.XPATH, "//ul[contains(@id, 'tabs_header_6511')][.//li[contains(@id, 'tab_6511_title_1')]][.//span]")
    liquids_tab.click()

    time.sleep(2)

    answer = driver.find_element(By.XPATH, "//div[.//p][.//strong]")
    
    # Verify if "Contact Us" page loaded
    assert "Always purchase liquids after you’ve passed the security checkpoint." in answer.get_attribute('innerHTML')