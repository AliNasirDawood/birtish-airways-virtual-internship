import requests
from bs4 import BeautifulSoup
from text_strip import text_strip_html_text


def fetch_html_content(url):
    """
    Fetch the HTML content from the provided URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}")
        return None


def extract_data(html_content):
    """
    Extract review data from the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    header = soup.find_all("h2", class_="text_header")
    author = soup.find_all("span", itemprop="name")
    country = soup.find_all("h3", class_="text_sub_header userStatusWrapper")
    date_published = soup.find_all("time", itemprop="datePublished")
    review_body = soup.find_all("div", class_="text_content")
    type_of_traveller = soup.find_all(
        "td", class_="review-rating-header type_of_traveller"
    )
    seat_type = soup.find_all("td", class_="review-rating-header cabin_flown")
    route = soup.find_all("td", class_="review-rating-header route")
    date_flown = soup.find_all("td", class_="review-rating-header date_flown")
    recommended = soup.find_all("td", class_="review-rating-header recommended")
    tr_rating_elements = soup.find_all("tr")
    return (
        header,
        author,
        country,
        date_published,
        review_body,
        type_of_traveller,
        seat_type,
        route,
        date_flown,
        recommended,
        tr_rating_elements,
    )


def html_parse_data(url):
    """
    Parse the provided URL and extract the data.
    """
    html_content = fetch_html_content(url)
    if html_content:
        (
            header,
            author,
            country,
            date_published,
            review_body,
            type_of_traveller,
            seat_type,
            route,
            date_flown,
            recommended,
            tr_rating_elements,
        ) = extract_data(html_content)
        text_strip_html_text(
            header,
            author,
            country,
            date_published,
            review_body,
            type_of_traveller,
            seat_type,
            route,
            date_flown,
            recommended,
            tr_rating_elements,
        )
    else:
        print("Failed to parse the data.")
