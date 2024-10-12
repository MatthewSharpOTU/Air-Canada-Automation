import time
import pytest
from utils.browserSetup import get_browser
from selenium.webdriver.common.by import By

# This file will run the test to see the answer in the Help page regarding 
# bringing liquids through security in your carry-on

# Base URL for Air Canada website
BASE_URL = "https://www.aircanada.com/"

# This function initializes test function to be called during runtime
# Return: Driver - Returns driver setup from browserSetup.py and gets website URL
@pytest.fixture
def setup():
    driver = get_browser()
    driver.get(BASE_URL)
    yield driver

# This function will traverse the website and help formums, switching tabs in the process
def test_contact_us_page_access(setup):
    # Setup Driver
    driver = setup
    # Wait 5 Seconds for Website to Load
    time.sleep(5)

    # Scroll to the bottom of the page to find "Help and Contact"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for Window to Scroll
    time.sleep(1)

    # Locate and Click the "Help and Contact" link
    contact_us_link = driver.find_element(By.LINK_TEXT, "Help And Contact")
    contact_us_link.click()

    # Wait 5 Seconds for Window to Load
    time.sleep(5)
    # Switch to new Window
    driver.switch_to.window(driver.window_handles[1])

    # Locate and Click the element the first element with "View all"
    page_traversal = driver.find_element(By.XPATH, "//a[text()[contains(., 'View all')]]")
    page_traversal.click()

    # Wait 1 second for element to appear
    time.sleep(1)
    # Scroll down the page
    driver.execute_script("window.scrollTo(0, 250);")

    # Wait for window to scroll
    time.sleep(1)

    page_traversal = driver.find_element(By.XPATH, "//a[text()[contains(., 'Carry-on baggage')]]")
    page_traversal.click()

    # Wait for New Window To Load
    time.sleep(5)
    # Switch to New Window
    driver.switch_to.window(driver.window_handles[2])

    # Locate and Click on the "Liquids and Gels Tab"
    liquids_tab = driver.find_element(By.XPATH, "//ul[contains(@id, 'tabs_header_6511')][.//li[contains(@id, 'tab_6511_title_1')]][.//span]")
    liquids_tab.click()

    # Retrieve the Desired Element
    answer = driver.find_element(By.XPATH, "//div[.//p][.//strong]")
    
    # Verify the answer to the customers query using the innerHTML
    assert "Always purchase liquids after you’ve passed the security checkpoint." in answer.get_attribute('innerHTML')