import pandas as pd
def _load_listings_data():
    df_listings = pd.read_csv(r'C:\Users\desktop\Downloads\listings_2_reduced.csv',low_memory=False)#
    return df_listings
def _load_reviews_data():
    df_reviews =  pd.read_csv(r'C:\Users\desktop\Downloads\reviews_2_reduced.csv',low_memory=False)#
    return df_reviews

def load_data():
    return _load_listings_data(),_load_reviews_data()


