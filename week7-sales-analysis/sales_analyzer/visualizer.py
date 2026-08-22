import matplotlib.pyplot as plt
import os

def create_visualizations(analyzer, output_dir='data/reports'):
    os.makedirs(output_dir, exist_ok=True)
    
    monthly = analyzer.monthly_trends()
    if not monthly.empty:
        plt.figure(figsize=(10, 5))
        monthly['total_amount'].plot(kind='line', marker='o', color='#1f77b4', linewidth=2)
        plt.title('Monthly Sales Trend (2024)', fontsize=14)
        plt.xlabel('Month')
        plt.ylabel('Total Sales ($)')
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'monthly_trend.png'))
        plt.close()

    category = analyzer.sales_by_category()
    if not category.empty:
        plt.figure(figsize=(7, 7))
        category['total_amount'].plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='tab10')
        plt.title('Revenue Share by Category', fontsize=14)
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'category_share.png'))
        plt.close()

    top_p = analyzer.top_products(5)
    if not top_p.empty:
        plt.figure(figsize=(10, 5))
        top_p['total_amount'].plot(kind='bar', color='#2ca02c')
        plt.title('Top 5 Performing Products', fontsize=14)
        plt.xlabel('Product')
        plt.ylabel('Revenue ($)')
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'top_products.png'))
        plt.close()
