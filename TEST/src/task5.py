import pandas as pd
from data_loader import load_data


# import warnings

# # Suppress specific warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)


def listings_with_best_expected_revenue(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> int:
    review_score_columns = [
    'minimum_nights',
    'id',
    'price'
    ]
    df_list_takk_1 = df_listings[review_score_columns].copy()

    df_list_takk_1['price'] = df_list_takk_1['price'].replace({'\\$': '', ',': ''}, regex=True).astype(float)
 
    # Filter listings with minimum_nights <= 7
    filtered_listings = df_list_takk_1[df_list_takk_1['minimum_nights'] <= 7]

    # Calculate the number of reviews for each listing
    review_counts = df_reviews['listing_id'].value_counts().reset_index()
    review_counts.columns = ['id', 'num_reviews']

    # Merge the review counts with the filtered listings
    merged_data = pd.merge(filtered_listings, review_counts, on='id', how='left')

    # Fill NaN values in num_reviews with 0 (for listings with no reviews)
    merged_data['num_reviews'] = merged_data['num_reviews'].fillna(0)

    # Calculate expected revenue
    # Assuming 60% of guests leave reviews, we can estimate the total number of guests
    # Total guests = num_reviews / 0.6
    # Expected revenue = Total guests * average nightly price * minimum_nights
    merged_data['expected_revenue'] = (merged_data['num_reviews'] / 0.6) * merged_data['price'] * merged_data['minimum_nights']

    # Identify the listing with the best expected revenue
    best_listing = merged_data.loc[merged_data['expected_revenue'].idxmax()]
    #result = best_listing['expected_revenue']
    result = best_listing.get('expected_revenue', 0)  # Default to 0 if not found
    # # Output the best listing details
    # print("Best Listing for Revenue:")
    # print(f"Listing ID: {best_listing['listing_id']}")
    # print(f"Expected Revenue: ${best_listing['expected_revenue']:.2f}")
    # print(f"Price per Night: ${best_listing['price']:.2f}")
    # print(f"Minimum Nights: {best_listing['minimum_nights']}")
    return int(result)


'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',listings_with_best_expected_revenue(*load_data()))