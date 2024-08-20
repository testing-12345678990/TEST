import pandas as pd
from data_loader import load_data


def host_attribute_with_second_highest_to_reviews(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:

    # Select relevant columns
    columns_of_interest = ['number_of_reviews', 'host_since', 'host_listings_count', 
                        'host_identity_verified', 'calculated_host_listings_count', 
                        'host_is_superhost']

    # Filter the DataFrame to include only the relevant columns
    df = df_listings[columns_of_interest].copy()

    #df['price'] = df['price'].replace({'\\$': '', ',': ''}, regex=True).astype(float)

    # Convert categorical variables to numerical representations
    # For 'host_identity_verified' and 'host_is_superhost', we can map them to 1 and 0
    df['host_identity_verified'] = df['host_identity_verified'].map({'t': 1, 'f': 0})
    df['host_is_superhost'] = df['host_is_superhost'].map({'t': 1, 'f': 0})

    # Convert 'host_since' to a numerical value (e.g., number of years since the host started)
    df['host_since'] = pd.to_datetime(df['host_since'])
    df['host_since'] = (pd.Timestamp.now() - df['host_since']).dt.days / 365  # Convert to years

    # Calculate correlations with 'number_of_reviews'
    correlations = df.corr()['number_of_reviews'].drop('number_of_reviews')

    # Sort correlations and get the second strongest
    sorted_correlations = correlations.abs().sort_values(ascending=False)
    second_strongest = sorted_correlations.index[1]  # Get the second strongest correlation
    # Find the highest correlated attribute
    highest_correlated = correlations.idxmax()  # Get the attribute with the highest correlation
        # Output the results
    # print("Correlations with number of reviews:")
    # print(correlations)
    # print(f"\nThe second strongest correlated host attribute with number of reviews is: '{second_strongest}'")
    return highest_correlated


'''
MANDATORY - Explain your solution in plain english here
'''
if __name__== '__main__':
    print('Review score with max correlation to price is:',host_attribute_with_second_highest_to_reviews(*load_data()))