from selenium.webdriver.common.by import By
from utils.selenium_setup import create_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_menu_titles():
    driver = create_driver()
    
    driver.get("https://www.24h.com.vn/")
    
    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    
    # Define the XPath to select all menu titles
    xpath = "//nav[@class='menu-24h-main']//ul/li/a"
    # Find all elements matching the XPath
    menu_elements = driver.find_elements(By.XPATH, xpath)
    # Extract the text from each element
    # Extract the text and URL from each element
    menu_items = [{"title": element.text, "url": element.get_attribute("href")} for element in menu_elements]

    #Return the list, with the titles and their corresponding URLS
    return menu_items

