from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_browser():
    # Setup Chrome WebDriver using ChromeDriverManager
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")  # Start browser maximized
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver