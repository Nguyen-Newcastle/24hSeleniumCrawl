from selenium.webdriver.common.by import By
from read_article_metadata import get_metadata_from_article
from utils.selenium_setup import create_driver, quit_driver

#Function to get all the current highlighted articles on the 24h website.
def get_highlighted_articles_metadata():
    
    driver = create_driver()

    try:
        # Navigate to the website
        driver.get("https://www.24h.com.vn/")

        # Define XPath to select all articles in the section
        article_xpath = "//section[@class='box-2coll-24h box-2coll-24h-t']//article[@class='hightl-24h-items']"

        # Find all article elements
        articles = driver.find_elements(By.XPATH, article_xpath)
        # List to store extracted article information
        article_data = []
        # Loop through each article and extract information
        for article in articles:
            title_element = article.find_element(By.XPATH, ".//header/h3/a")
            title = title_element.text
            url = title_element.get_attribute("href")

            title = {"Title": title}
            article_metadata = get_metadata_from_article(url)
            final_article_metadata = {**title, **article_metadata}
            article_data.append(final_article_metadata)

    finally:
        # Close the WebDriver
        quit_driver(driver)

    return article_data


def main():
    print(get_highlighted_articles_metadata())

if __name__ == "__main__":
    main()