import pandas as pd

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    def get_basic_stats(self):
        stats = {
            'total_sales': self.df['total_amount'].sum(),
            'total_orders': len(self.df),
            'avg_order_value': self.df['total_amount'].mean(),
            'unique_customers': self.df['customer_id'].nunique(),
            'unique_products': self.df['product_name'].nunique()
        }
        if 'order_date' in self.df.columns:
            stats['start_date'] = self.df['order_date'].min().strftime('%Y-%m-%d')
            stats['end_date'] = self.df['order_date'].max().strftime('%Y-%m-%d')
        return stats

    def sales_by_category(self):
        return self.df.groupby('category').agg({
            'total_amount': 'sum',
            'quantity': 'sum',
            'order_id': 'count'
        }).rename(columns={'order_id': 'order_count'}).sort_values(by='total_amount', ascending=False)

    def top_products(self, n=5):
        return self.df.groupby('product_name').agg({
            'total_amount': 'sum',
            'quantity': 'sum'
        }).sort_values(by='total_amount', ascending=False).head(n)

    def monthly_trends(self):
        df_copy = self.df.copy()
        df_copy['month_year'] = df_copy['order_date'].dt.to_period('M')
        monthly = df_copy.groupby('month_year').agg({
            'total_amount': 'sum',
            'quantity': 'sum',
            'order_id': 'count',
            'customer_id': 'nunique'
        }).rename(columns={'order_id': 'order_count', 'customer_id': 'unique_customers'})
        
        monthly['growth_rate'] = monthly['total_amount'].pct_change() * 100
        return monthly
