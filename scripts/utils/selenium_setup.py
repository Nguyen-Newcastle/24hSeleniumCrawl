from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_driver():

    #Creating options for Chrome.
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.set_capability("browserName", "chrome")

    max_retries = 10
    retry_delay = 4
    for i in range(max_retries):
        try:
            driver = webdriver.Remote(
                command_executor='http://selenium-hub:4444/wd/hub',
                options=chrome_options
            )
            return driver
        except Exception as e:
            logger.warning(f"Attempt {i + 1} to connect to Selenium Hub failed: {e}")
            time.sleep(retry_delay)
    raise Exception(f"Failed to connect to Selenium Hub after {max_retries} retries")

def quit_driver(driver):
    try:
        driver.quit()
    except Exception as e:
        logger.error(f"Error while quitting driver: {e}")
