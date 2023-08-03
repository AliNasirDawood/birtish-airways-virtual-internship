from selenium import webdriver
from selenium.webdriver.common.by import By
from htmlparsedata import html_parse_data

def get_total_pages(driver, url):
    """
    Navigate to the website with pagination and retrieve the total number of pages.
    """
    driver.get(url)
    total_pages_element = driver.find_element(By.XPATH, '//*[@id="main"]/section[3]/div[1]/div/article/ul')
    total_pages_text = total_pages_element.text
    return int(total_pages_text.split()[-2])  # Assuming the last word is the total number of pages

def scrape_reviews_for_all_pages(driver, base_url, total_pages):
    """
    Scrape reviews for all pages and call the html_parse_data function.
    """
    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}/page/{page_num}/?sortby=post_date%3ADesc&pagesize=500"
        driver.get(page_url)
        print(f'Page Number = {page_num}')
        print(f'Page URL = {page_url}')
        print(f"The length of the page = {len(page_url)}")
        print(f"The Type of the page = {type(page_url)}")
        html_parse_data(page_url)

def main():
    # Start a Chrome WebDriver
    driver = webdriver.Chrome()

    base_url = 'https://www.airlinequality.com/airline-reviews/british-airways/'
    total_pages = get_total_pages(driver, base_url)
    scrape_reviews_for_all_pages(driver, base_url, total_pages)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
