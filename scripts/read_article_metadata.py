from utils.selenium_setup import create_driver, quit_driver
from selenium.webdriver.common.by import By
import json

def get_metadata_from_article(article_url):

    # Navigate to the article page
    #Create the Selenium Grid driver to get access to the article URL.
    driver = create_driver()
    driver.get(article_url)

    # Extract meta description
    description = driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute('content')

    # Extract canonical URL
    url = driver.find_element(By.XPATH, "//link[@rel='canonical']").get_attribute('href')

    # Extract Open Graph image
    og_image = driver.find_element(By.XPATH, "//meta[@property='og:image']").get_attribute('content')

    # Extract date published and date modified
    date_published = driver.find_element(By.XPATH, "//meta[@itemprop='datePublished']").get_attribute('content')
    date_modified = driver.find_element(By.XPATH, "//meta[@itemprop='dateModified']").get_attribute('content')

    # Extract JSON-LD structured data
    json_ld_script = driver.find_element(By.XPATH, "//script[@type='application/ld+json']").get_attribute('innerHTML')
    json_ld_data = json.loads(json_ld_script)

    # Extract information from JSON-LD
    headline = json_ld_data['headline']
    date_created = json_ld_data['dateCreated']
    author = json_ld_data['author']['name']
    publisher = json_ld_data['publisher']['name']
    publisher_logo = json_ld_data['publisher']['logo']['url']
    article_image = json_ld_data['image']['url']
    
    # Extract and concatenate content paragraphs with <p> tag and no attributes
    content_elements = driver.find_elements(By.XPATH, './/p[not(@*)]')
    article_content = '\n'.join([content.text for content in content_elements])
    
    # Close the WebDriver
    quit_driver(driver)

    # Print extracted information
    return {"Description:": description, "URL": url, "Open Graph Image:": og_image, 
            "Date Published:": date_published, "DateCreated": date_created,
           "Date Modified:": date_modified, "Headline:": headline, 
           "Author:": author, "Publisher:": publisher, "Article Image:": article_image,
           "Article Content": article_content}