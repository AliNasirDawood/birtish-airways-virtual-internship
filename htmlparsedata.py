import requests
from bs4 import BeautifulSoup
from text_strip import text_strip_html_text


def html_parse_data(url):

    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting the information
    header = soup.find_all('h2', class_='text_header')
    author = soup.find_all('span', itemprop='name')
    country = soup.find_all('h3', class_='text_sub_header userStatusWrapper')
    date_published = soup.find_all('time', itemprop='datePublished')
    review_body = soup.find_all('div', class_='text_content')
    type_of_traveller = soup.find('td', class_='review-rating-header type_of_traveller').find_next_sibling('td')
    seat_type = soup.find('td', class_='review-rating-header cabin_flown').find_next_sibling('td')
    route = soup.find('td', class_='review-rating-header route').find_next_sibling('td')
    date_flown = soup.find('td', class_='review-rating-header date_flown').find_next_sibling('td')
    recommended = soup.find('td', class_='review-rating-header recommended').find_all_next_sibling('td')

    # Printing the extracted information
    text_strip_html_text(header,author,country,date_published,review_body,type_of_traveller,seat_type,route,date_flown,recommended)
     

    # tr_elements = soup.find_all('tr')

    # for tr in tr_elements:
    #     header_td = tr.find('td', class_='review-rating-header')
    #     rating_td = tr.find('td', class_='review-rating-stars')
    #     filled_stars = len(rating_td.find_all('span', class_='star fill'))
    #     print(f"{header_td.text.strip()}\t{filled_stars}")