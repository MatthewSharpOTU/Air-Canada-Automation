from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function sets up Chrome WebDriver using ChromeDriverManager
# Return: Driver - Chrome WebDriver configured with provided options
def get_browser():
    options = Options()
    options.add_experimental_option("detach", True)     # Browser will stay open after completion
    options.add_argument("--start-maximized")           # Start browser maximized
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver