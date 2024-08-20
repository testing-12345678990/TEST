import pandas as pd

def df_test_1():
    df_listings = pd.DataFrame({
                'id': [1, 2, 3, 4, 5],
                'name': ['Cozy Apartment', 'Modern House', 'Beachside Retreat', 'City Center Studio', 'Family Friendly Hom'],
                'description': ['Charming apartment in the heart of the city', 'Spacious house with modern amenities',"Relaxing beachside retreat with stunning views", 'Convenient studio in the city center','Spacious home ferfect for families'],
                'host_id': [123, 456, 789, 1011, 1213],
                'host_is_superhost': ['f', 't','f', 'f', 'f'],
                'host_identity_verified': ['t','t','t', 'f', 't'],
                'host_since': ['2011-04-10', '2011-04-10', '2010-07-17', '2010-07-04', "2011-08-03"],
                'host_listings_count': [10, 20, 30, 15, 25],
                'calculated_host_listings_count': [10, 20, 28, 15, 22],
                'price': ["$100.00", "$1,500.00", "$200.00", "$25.00", "$182.00"],
                'neighbourhood_cleansed': ['Hollywood', 'Hollywood', 'South Beach', 'The Loop', 'Pacific Heights'],
                'country': ['US', 'US','US', 'US','US'],
                'property type': ['Apartment', 'House', 'Condo', "Studio", 'House'],
                'room_typ': ['Private room', 'Entire home/apt', 'Entire home/apt', 'Private room', 'Entire home/apt'],
                'minimum_nights': [3, 5, 7, 3, 5],
                'review_scores_rating': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review_scores_cleanliness': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review_scores_checkin': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review scores communication': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review_scores_location': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review_scores_location': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review scores value': [4.5, 4.8, 4.9, 4.7, 4.6],
                'review scores accuracy': [4.5, 4.8, 4.9, 4.7, 4.6],
                'number_of reviews': [10, 20, 38, 15, 25]})
    return df_listings

def df_test_2():
    df_reviews = pd.DataFrame({
    'id': [10, 20, 30, 40, 50],
    'listing_id': [1, 2, 3, 4, 5],
    'date': ['2020-01-01', '20201-15', '2020-02-01', '2020-03-01', '2020-03-15'],
    'reviewer_id': [123, 456, 789, 1011, 1213],
    'reviewer_name': ['John', 'Jane', 'Bob', 'Alice', 'Mike'],
    'review': ['Great place!', 'Awesome host!', 'Clean and comfortable', 'Perfect location', 'Cozy apartment'],
    'rating': [5, 5, 4, 5, 4]
    })
    return df_reviews

def load_data():
    return df_test_1(),df_test_2()