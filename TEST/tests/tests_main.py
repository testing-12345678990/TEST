import numpy as np
import pandas as pd
import unittest

import sys
import os
# sys.path.append('.')
# sys.path.append("..")

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestMain(unittest.TestCase):
    def setUpClass ():
        TestMain.df_listings  = pd.DataFrame({
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
            'room_type': ['Private room', 'Entire home/apt', 'Entire home/apt', 'Private room', 'Entire home/apt'],
            'minimum_nights': [3, 5, 7, 3, 5],
            'review_scores_rating': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_cleanliness': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_checkin': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_communication': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_location': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_value': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_accuracy': [4.5, 4.8, 4.9, 4.7, 4.6],
            'number_of_reviews': [10, 20, 38, 15, 25]
        })

        TestMain.df_reviews = pd.DataFrame({
            'id': [10, 20, 30, 40, 50],
            'listing_id': [1, 2, 3, 4, 5],
            'date': ['2020-01-01', '20201-15', '2020-02-01', '2020-03-01', '2020-03-15'],
            'reviewer_id': [123, 456, 789, 1011, 1213],
            'reviewer_name': ['John', 'Jane', 'Bob', 'Alice', 'Mike'],
            'review': ['Great place!', 'Awesome host!', 'Clean and comfortable', 'Perfect location', 'Cozy apartment'],
            'rating': [5, 5, 4, 5, 4]
            })

    def _float_equals( a, b, epsilon = 1e-9):
        return abs(a - b) < epsilon
    _float_equals = staticmethod(_float_equals) 
    def run(self, result=None):
        """Override the run method to print detailed output."""
        test_name = self._testMethodName
        print(f"Running test: {test_name}")
        super().run(result)
        if result.wasSuccessful():
            print(f"Test {test_name} passed.")
        else:
            print(f"Test {test_name} failed.")

    def test_task1(self):
        from task1 import review_score_with_highest_correlation_to_price
        result = review_score_with_highest_correlation_to_price(TestMain.df_listings.copy(),TestMain.df_reviews.copy())
        self.assertEqual (result, 'Hollywood' ) 
    def test_task2(self):
        from task2 import review_score_with_highest_correlation_to_price_2
        result = review_score_with_highest_correlation_to_price_2(TestMain.df_listings.copy(),TestMain.df_reviews.copy())
        self.assertEqual (result, 'review_scores_rating' )

    # def test_task3(self):
    #     task3 = __import__('src.task3').task3
    #     result = task3.prof_non_prof_host_price_diff(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
    #     self.assertTrue(TestMain._float_equals(result, -401.00, 0.1))    

    def test_task3(self):
        from task3 import prof_non_prof_host_price_diff
        result = prof_non_prof_host_price_diff(self.df_listings.copy(), self.df_reviews.copy())
        # self.assertAlmostEqual(result, -401.00,0.1) 
        self.assertTrue(TestMain._float_equals(result, -401.00, 0.1))   
    def test_task4(self):
        from task4 import median_price_premium
        result = median_price_premium(self.df_listings.copy(), self.df_reviews.copy())
        self.assertTrue(TestMain._float_equals(result,1400.00,0.2)) 
    def test_task5(self):
        from task5 import listings_with_best_expected_revenue
        result = listings_with_best_expected_revenue(self.df_listings.copy(), self.df_reviews.copy())
        self.assertTrue((result,0)) 

    def test_task6(self):
        from task6 import avg_diff_superhost_nonsuperhost_review_score
        result = avg_diff_superhost_nonsuperhost_review_score(self.df_listings.copy(), self.df_reviews.copy())
        # self.assertAlmostEqual(result, -401.00,0.1) 
        self.assertTrue(TestMain._float_equals(result,0.12, 0.1))       
    def test_task7(self):
        from task7 import host_attribute_with_second_highest_to_reviews
        result = host_attribute_with_second_highest_to_reviews(TestMain.df_listings.copy(),TestMain.df_reviews.copy())
        self.assertEqual (result, 'calculated_host_listings_count' )
if __name__== '__main__':
    unittest.main()

        
