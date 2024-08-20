import pandas as pd
from data_loader import load_data

# Write your code here
def review_score_with_highest_correlation_to_price(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
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
'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',review_score_with_highest_correlation_to_price(*load_data()))









