from utils.selenium_setup import create_driver, quit_driver
from selenium.webdriver.common.by import By
from read_article_metadata import get_metadata_from_article
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_menu_titles import read_menu_titles
from concurrent.futures import ThreadPoolExecutor, as_completed

#Function to get the latest articles on all sections of the 24h website(Currently)
def get_latest_articles_on_sections(section_url):
    
    # Initialize WebDriver with Selenium Grid
    driver = create_driver()
    driver.get(section_url)
    
    try:
        # Introduce a random delay to control request frequency
        time.sleep(random.uniform(1, 1.5))  # Delay between 1 and 3 seconds
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Define XPath to select all articles in the "latest articles" section
        article_xpath = "//div[@class='cate-24h-foot-home-latest-list']//article"

        # Find all article elements
        articles = driver.find_elements(By.XPATH, article_xpath)

        # List to store extracted article information
        article_data = []

        # Loop through each article and extract information
        for article in articles:
            article_url = article.find_element(By.XPATH, './/figure/a').get_attribute('href')

            #Extract title
            title_element = article.find_element(By.XPATH, ".//header/h3/a")
            title = title_element.text
            
            #Apply get_metadata_from_article() to get the metadata for the article, append it into the list.
            title = {"Title": title}
            article_metadata = get_metadata_from_article(article_url)
            final_article_metadata = {**title, **article_metadata}
            article_data.append(final_article_metadata)

    finally:
         # Close the WebDriver
        quit_driver(driver)

    return article_data 


MENU_TITLES = read_menu_titles()
URLS = [topic["url"] for topic in MENU_TITLES]

# Function to run concurrent scraping tasks with controlled frequency
def run_concurrent_tasks(urls, max_workers=5):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(get_latest_articles_on_sections, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results.append((url, data))
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
    
    return results


def main():
    print(run_concurrent_tasks(URLS, max_workers = 2))

if __name__ == "__main__":
    main()