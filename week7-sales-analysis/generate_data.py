import os
import pandas as pd
import numpy as np

os.makedirs('data/raw', exist_ok=True)

np.random.seed(42)
n_rows = 1200

dates = pd.date_range(start='2024-01-01', end='2024-12-31', periods=n_rows)
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports']
products = {
    'Electronics': ['Laptop Pro', 'Smartphone X', 'Wireless Headphones', 'Tablet Air', 'Smart Watch'],
    'Clothing': ['Denim Jacket', 'Cotton T-Shirt', 'Running Shoes', 'Winter Coat', 'Casual Hoodie'],
    'Home & Garden': ['Coffee Maker', 'Desk Lamp', 'Air Purifier', 'Indoor Plant', 'Vacuum Cleaner'],
    'Books': ['Python Programming', 'Data Science Guide', 'Novel Best Seller', 'History Anthology', 'Design Patterns'],
    'Sports': ['Yoga Mat', 'Dumbbell Set', 'Bicycle', 'Tennis Racket', 'Water Bottle']
}

cat_choice = np.random.choice(categories, size=n_rows)
prod_choice = [np.random.choice(products[c]) for c in cat_choice]
quantities = np.random.randint(1, 10, size=n_rows)
unit_prices = np.random.uniform(10.0, 500.0, size=n_rows).round(2)
total_amounts = (quantities * unit_prices).round(2)
customer_ids = [f"CUST-{np.random.randint(100, 300)}" for _ in range(n_rows)]
order_ids = [f"ORD-{1000 + i}" for i in range(n_rows)]

df = pd.DataFrame({
    'order_id': order_ids,
    'customer_id': customer_ids,
    'order_date': dates.strftime('%Y-%m-%d'),
    'category': cat_choice,
    'product_name': prod_choice,
    'quantity': quantities,
    'unit_price': unit_prices,
    'total_amount': total_amounts
})

df.loc[10:15, 'total_amount'] = np.nan
df.loc[25:28, 'category'] = np.nan
df = pd.concat([df, df.iloc[50:55]], ignore_index=True)

df.to_csv('data/raw/sales_data.csv', index=False)
print("Sample raw sales dataset created at data/raw/sales_data.csv")
