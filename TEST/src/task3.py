import pandas as pd
from data_loader import load_data

def prof_non_prof_host_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    
    
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
    return int(price_difference)
'''

MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',prof_non_prof_host_price_diff(*load_data()))









