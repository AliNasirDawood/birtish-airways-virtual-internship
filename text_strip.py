import bs4
import re
import pandas as pd
import os

def text_strip_html_text(header,author,country,date_published,review_body,type_of_traveller,seat_type,route,date_flown,recommended,tr_rating_elements):

    
    passenger_names = [author_text.text.strip() for author_text in author]
    date = [date_published_text.text.strip() for date_published_text in date_published]
    raw_country = [country_text.text.strip() for country_text in country]
    updated_country = [re.search(r'\((.*?)\)', entry).group(1) for entry in raw_country]
    traveller = [type_of_traveller_data.find_next_sibling('td').text for type_of_traveller_data in type_of_traveller]
    seat_type = [seat_type_data.find_next_sibling('td').text for seat_type_data in seat_type]
    route = [route_data.find_next_sibling('td').text for route_data in route]
    date_flown = [date_flown_data.find_next_sibling('td').text for date_flown_data in date_flown ]
    recommendation = [recommended_data.find_next_sibling('td').text for recommended_data in recommended]
    review = [review_body_data.text for review_body_data in review_body]
    title = [header_text.text.strip() for header_text in header]
    

    ratings = [(header_td.text.strip(), len(rating_td.find_all('span', class_='star fill'))) for tr in tr_rating_elements
           for header_td in [tr.find('td', class_='review-rating-header')]
           for rating_td in [tr.find('td', class_='review-rating-stars')]
           if header_td is not None and rating_td is not None]
    print(ratings)

    data = {"Passenger Name": passenger_names, "Date": date,"Country":updated_country,
            "Type of Traveller":traveller,"Seat Type":seat_type,"Route":route,
            'Date Flown':date_flown,'Recommended':recommendation,'Comment':title,'Review':review}
    df = pd.DataFrame(data)
    df['Trip Type'] = df['Review'].apply(lambda x: 'Trip Verified' if 'Trip Verified' in x else 'Not Verified')
    df['Review'] = df['Review'].str.replace('✅ Trip Verified |', '').str.replace('Not Verified |', '')



    print(df)
# Specify the file path for the CSV file
    file_path = 'data.csv'

        # Check if the file already exists
    if os.path.isfile(file_path):
        # If the file exists, append the data to it
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # If the file doesn't exist, create a new file and save the data
        df.to_csv(file_path, index=False)
        # for header, filled_stars in ratings:
    #     print(f"{header} = {filled_stars}")

