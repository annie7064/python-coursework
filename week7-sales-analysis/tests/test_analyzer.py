import unittest
import pandas as pd
from sales_analyzer import clean_data, SalesAnalyzer

class TestSalesAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'order_id': ['O1', 'O2', 'O2'],
            'customer_id': ['C1', 'C2', 'C2'],
            'order_date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-02']),
            'category': ['Electronics', 'Books', 'Books'],
            'product_name': ['Laptop', 'Book A', 'Book A'],
            'quantity': [1, 2, 2],
            'unit_price': [1000.0, 20.0, 20.0],
            'total_amount': [1000.0, 40.0, 40.0]
        })

    def test_clean_data(self):
        cleaned, dedup = clean_data(self.sample_data)
        self.assertEqual(dedup, 1)
        self.assertEqual(len(cleaned), 2)

    def test_basic_stats(self):
        cleaned, _ = clean_data(self.sample_data)
        analyzer = SalesAnalyzer(cleaned)
        stats = analyzer.get_basic_stats()
        self.assertEqual(stats['total_sales'], 1040.0)
        self.assertEqual(stats['unique_customers'], 2)

if __name__ == '__main__':
    unittest.main()
