import pandas as pd
from data_loader import load_data
# import sys
# import os

# sys.path.append('.')
# sys.path.append("..")
# from test_data.test_df import load_data
def median_price_premium(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    # Filter for entire homes/apartments and other types
    entire_homes = df_listings[df_listings['room_type'] == 'Entire home/apt'].copy()
    other_listings = df_listings[df_listings['room_type'] != 'Entire home/apt'].copy()
    
    # Convert price to numeric (removing $ and commas)
    entire_homes['price'] = entire_homes['price'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
    other_listings['price'] = other_listings['price'].replace({'\\$': '', ',': ''}, regex=True).astype(float)

    #df_list_takk_1['price'] = df_list_takk_1['price'].replace({r'\$': '', ',': ''}, regex=True).astype(float)
    
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
    print('Review score with max correlation to price is:',median_price_premium(*load_data()))

