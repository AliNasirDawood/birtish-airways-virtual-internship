import re
import pandas as pd
import os

def extract_review_data(header, author, country, date_published, review_body, type_of_traveller, seat_type, route, date_flown, recommended, tr_rating_elements):
    """
    Extracts review data from the provided lists using BeautifulSoup.
    Returns a dictionary with the extracted data.
    """
    passenger_names = [author_text.text.strip() for author_text in author]
    date = [date_published_text.text.strip() for date_published_text in date_published]
    raw_country = [country_text.text.strip() for country_text in country]
    updated_country = [re.search(r'\((.*?)\)', entry).group(1) if re.search(r'\((.*?)\)', entry) else None for entry in raw_country]
    traveller = [type_of_traveller_data.find_next_sibling('td').text for type_of_traveller_data in type_of_traveller]
    seat_type = [seat_type_data.find_next_sibling('td').text for seat_type_data in seat_type]
    route = [route_data.find_next_sibling('td').text for route_data in route]
    date_flown = [date_flown_data.find_next_sibling('td').text for date_flown_data in date_flown]
    recommendation = [recommended_data.find_next_sibling('td').text for recommended_data in recommended]
    review = [review_body_data.text for review_body_data in review_body]
    title = [header_text.text.strip() for header_text in header]

    data = {
        "Passenger Name": passenger_names,
        "Date": date,
        "Country": updated_country,
        "Type of Traveller": traveller,
        "Seat Type": seat_type,
        "Route": route,
        'Date Flown': date_flown,
        'Recommended': recommendation,
        'Comment': title,
        'Review': review
    }

    return data

def clean_and_save_data(data):
    """
    Cleans the data, creates a DataFrame, and saves it to a CSV file.
    """
    # Find the maximum length among all arrays
    max_length = max(len(value) for value in data.values())

    # Fill arrays with None until they have the same length
    for key in data.keys():
        data[key] = data[key] + [None] * (max_length - len(data[key]))

    df = pd.DataFrame(data)
    df['Trip Type'] = df['Review'].apply(lambda x: 'Trip Verified' if 'Trip Verified' in x else 'Not Verified')
    df['Review'] = df['Review'].str.replace('✅ Trip Verified |', '').str.replace('Not Verified |', '')

    # Specify the file path for the CSV file
    file_path = 'data.csv'

    # Check if the file already exists
    if os.path.isfile(file_path):
        # If the file exists, append the data to it
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # If the file doesn't exist, create a new file and save the data
        df.to_csv(file_path, index=False)

def text_strip_html_text(header, author, country, date_published, review_body, type_of_traveller, seat_type, route, date_flown, recommended, tr_rating_elements):
    """
    Main function that orchestrates the data extraction and cleaning process.
    """
    data = extract_review_data(header, author, country, date_published, review_body, type_of_traveller, seat_type, route, date_flown, recommended, tr_rating_elements)
    print(data)
    print(len(data))
    print(type(data))
    print(data.keys())
    lengths = {key: len(value) for key, value in data.items()}

    # Print the lengths of each key
    for key, length in lengths.items():
        print(f"{key}: {length}")

    clean_and_save_data(data)
