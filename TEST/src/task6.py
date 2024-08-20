import pandas as pd
from data_loader import load_data

def avg_diff_superhost_nonsuperhost_review_score(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    review_score_columns = [
    'id',
    'minimum_nights',
    'host_is_superhost',
    'review_scores_rating',
    'price'
    ]
    df_list_takk_1 = df_listings[review_score_columns].copy()
    df_list_takk_1['price'] = df_list_takk_1['price'].replace({'\\$': '', ',': ''}, regex=True).astype(float)

    # Rename a single column
    # df_reviews.rename(columns={'listing_id': 'id'}, inplace=True)

    # Merge listings with reviews to get review scores
    merged_data = pd.merge(df_list_takk_1, df_reviews, on='id', how='left')

    # Calculate average review scores for superhosts and normal hosts
    superhost_scores = merged_data[merged_data['host_is_superhost'] == 't']['review_scores_rating'].mean()
    normalhost_scores = merged_data[merged_data['host_is_superhost'] == 'f']['review_scores_rating'].mean()

    # Calculate the average difference
    average_difference = superhost_scores - normalhost_scores

    # Output the results
    # print("Average Review Scores:")
    # print(f"Superhosts: {superhost_scores:.2f}")
    # print(f"Normal Hosts: {normalhost_scores:.2f}")
    # print(f"Average Difference: {average_difference:.2f}")
    return average_difference

'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',avg_diff_superhost_nonsuperhost_review_score(*load_data()))