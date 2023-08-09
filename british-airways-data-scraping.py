from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from htmlparsedata import html_parse_data


driver = webdriver.Chrome()

# Navigate to the website with pagination
driver.get("https://www.airlinequality.com/airline-reviews/british-airways")

# Locate the element that displays the total number of pages
# Update the XPath expression to match the actual element on the website
total_pages_element = driver.find_element(
    By.XPATH, '//*[@id="main"]/section[3]/div[1]/div/article/ul'
)

# Extract the text of the total pages element
total_pages_text = total_pages_element.text

# Process the extracted text to get the total number of pages
# You may need to parse the text and extract the numeric value
total_pages = int(
    total_pages_text.split()[-2]
)  # Assuming the last word is the total number of pages
for page_num in range(total_pages):
    page_url = (
        "https://www.airlinequality.com/airline-reviews/british-airways/page/"
        + str(page_num)
    )
    driver.get(page_url)
    print("Page Number  = ", page_num)
    print(page_url)
    html_parse_data(page_url)
# Close the browser
driver.quit()
