import pandas as pd
from data_loader import load_data
# import sys
# import os

# sys.path.append('.')
# sys.path.append("..")
# from test_data.test_df import load_data

# Write your code here
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
'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',review_score_with_highest_correlation_to_price_2(*load_data()))









