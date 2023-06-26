import bs4


def text_strip_html_text(header,author,country,date_published,review_body,type_of_traveller,seat_type,route,date_flown,recommended):
    for header_text in header:
        print(header_text.text.strip())
    for author_text in author:
        print(author_text.text.strip())
    for date_published_text in date_published:
        print(date_published_text.text.strip())
    for review_body_text in review_body:
        print(review_body_text.text.strip())
    for type_of_traveller_text in type_of_traveller:
        print(type_of_traveller_text.text.strip())
    for seat_type_text in seat_type:
        print(seat_type_text.text.strip())
    for route_text in route:
        print(route_text.text.strip())
    for date_flown_text in date_flown:
        print(date_flown_text.text.strip())
    for recommended_text in recommended:
        print(recommended_text.text.strip())
    