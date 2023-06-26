from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from htmlparsedata import html_parse_data


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
urls = [
    'https://www.airlinequality.com/airline-reviews/british-airways',
    # 'https://www.airlinequality.com/seat-reviews/british-airways',
    # 'https://www.airlinequality.com/lounge-reviews/british-airways'
]

# Open the webpages
for url in urls:
    driver.get(url)
    html_parse_data(url)


# Close the browser
driver.quit()

