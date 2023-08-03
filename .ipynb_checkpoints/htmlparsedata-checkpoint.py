import requests
from bs4 import BeautifulSoup
from text_strip import text_strip_html_text



def html_parse_data(url):

    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
 

    # # Extracting the information
    header = soup.find_all('h2', class_='text_header')
    author = soup.find_all('span', itemprop='name')
    country = soup.find_all('h3', class_='text_sub_header userStatusWrapper')
    date_published = soup.find_all('time', itemprop='datePublished')
    review_body = soup.find_all('div', class_='text_content')
    type_of_traveller = soup.find_all('td', class_='review-rating-header type_of_traveller')
    seat_type = soup.find_all('td', class_='review-rating-header cabin_flown')
    route = soup.find_all('td', class_='review-rating-header route')
    date_flown = soup.find_all('td', class_='review-rating-header date_flown')
    recommended = soup.find_all('td', class_='review-rating-header recommended')
    tr_rating_elements = soup.find_all('tr')
    # Printing the extracted information
   

            text_strip_html_text(header,author,country,date_published,review_body,type_of_traveller,seat_type,route,date_flown,recommended,tr_rating_elements)
     


