import pandas as pd
import sys
import os

sys.path.append('.')
sys.path.append("..")
# Add the path to the src directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#sys.path.insert(0, '../')  # assuming the parent directory is one level up
from test_data.test_df import load_data
#from src.data_loader import load_data

# def testt(df_list,df_review):
#     col = df_list.columns
#     return col


# Write your code here
def review_score_with_highest_correlation_to_price(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    df_list_takk_1 = df_listings[['neighbourhood_cleansed', 'host_is_superhost', 'price']].copy()

    df_list_takk_1['price'] = df_list_takk_1['price'].apply(lambda x: x.replace('$', '').replace(',', ''))
    df_list_takk_1['price'] = df_list_takk_1['price'].astype(float)

    # Group the data by neighbourhood and host_is_superhost
    median_prices = df_list_takk_1.groupby(['neighbourhood_cleansed', 'host_is_superhost'])['price'].median().reset_index()

    # pivot to have superhost and non-superhost prices in separate columns
    pivot_df = median_prices.pivot(index='neighbourhood_cleansed', \
                               columns='host_is_superhost', \
                               values='price')  
    # calculate price difference between superhosts and non-superhosts
    pivot_df['price_diff'] = pivot_df['f'] - pivot_df['t']

    max_diff_neighborhood = pivot_df['price_diff'].idxmax()

    return max_diff_neighborhood  


def review_score_with_highest_correlation_to_price_2(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    # Define the review score columns to analyze
    review_score_columns = [
    'review_scores_rating',
    'review_scores_accuracy',
    'review_scores_cleanliness',
    'review_scores_checkin',
    'review_scores_communication',
    'review_scores_location',
    'review_scores_value',
    'price'
    ]
    df_list_takk_1 = df_listings[review_score_columns].copy()
    df_list_takk_1['price'] = df_list_takk_1['price'].apply(lambda x: x.replace('$', '').replace(',', ''))
    df_list_takk_1['price'] = df_list_takk_1['price'].astype(float)

    # Calculate the correlation of the review scores with price
    correlation_with_price = df_list_takk_1[review_score_columns ].corr()['price']#+ ['price']
 

   # Find the review score with the strongest correlation to price
    strongest_correlation = correlation_with_price.drop('price').abs().idxmax()
    strongest_correlation_value = correlation_with_price[strongest_correlation]

    #print(f"The review score with the strongest correlation to price is '{strongest_correlation}' with a correlation of {strongest_correlation_value:.2f}.")

    return strongest_correlation  


def prof_non_prof_host_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    
    
    required_columns = ['host_id', 'neighbourhood_cleansed', 'price']
    listings_filtered = df_listings[required_columns].copy()

    listings_filtered['price'] = listings_filtered['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

    # Step 1: Identify professional hosts
    # Count the number of unique neighborhoods for each host
    host_neighborhood_counts = listings_filtered.groupby('host_id')['neighbourhood_cleansed'].nunique()

    # Classify hosts as professional or non-professional
    professional_hosts = host_neighborhood_counts[host_neighborhood_counts > 5].index
    listings_filtered['host_type'] = listings_filtered['host_id'].apply(lambda x: 'Professional' if x in professional_hosts else 'Non-Professional')

    # Step 2: Calculate average prices for professional and non-professional hosts
    average_prices = listings_filtered.groupby('host_type')['price'].mean()


    # Initialize default values
    avg_professional_price = average_prices.get('Professional', 0)  # Default to 0 if not found
    avg_non_professional_price = average_prices.get('Non-Professional', 0)  # Default to 0 if not found


    # Step 3: Calculate the price difference
    price_difference = avg_professional_price - avg_non_professional_price

    # Output the results
    # print(f"Average price for Professional Hosts: ${average_prices['Professional']:.2f}")
    # print(f"Average price for Non-Professional Hosts: ${average_prices['Non-Professional']:.2f}")
    # print(f"Average price difference: ${price_difference:.2f}")
    # Format to two decimal places
    # Round down to two decimal places
    rounded_number = int(price_difference)

    return rounded_number


###task 4
def median_price_premium(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    # Filter for entire homes/apartments and other types
    entire_homes = df_listings[df_listings['room_type'] == 'Entire home/apt'].copy()
    other_listings = df_listings[df_listings['room_type'] != 'Entire home/apt'].copy()
    
    # Convert price to numeric (removing $ and commas)
    entire_homes['price'] = entire_homes['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    other_listings['price'] = other_listings['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    
    # Group by neighborhood and calculate median prices
    median_entire_homes = entire_homes.groupby('neighbourhood_cleansed')['price'].median()
    median_other_listings = other_listings.groupby('neighbourhood_cleansed')['price'].median()
    
    # Create a DataFrame to compare medians
    median_comparison = pd.DataFrame({
        'median_entire_homes': median_entire_homes,
        'median_other_listings': median_other_listings
    }).dropna()  # Drop neighborhoods that don't have both types of listings
    
    # Calculate the price premium
    median_comparison['price_premium'] = median_comparison['median_entire_homes'] - median_comparison['median_other_listings']
    
    # Return the average price premium across all neighborhoods
    return median_comparison['price_premium'].mean()


'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',review_score_with_highest_correlation_to_price_2(*load_data()))









