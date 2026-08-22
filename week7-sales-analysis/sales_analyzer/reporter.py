import pandas as pd
import os

def export_excel_report(analyzer, output_path='data/reports/sales_report.xlsx'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        pd.DataFrame([analyzer.get_basic_stats()]).to_excel(writer, sheet_name='Summary', index=False)
        analyzer.sales_by_category().to_excel(writer, sheet_name='Category Sales')
        analyzer.top_products(10).to_excel(writer, sheet_name='Top Products')
        
        monthly = analyzer.monthly_trends()
        monthly.index = monthly.index.astype(str)
        monthly.to_excel(writer, sheet_name='Monthly Trends')

def print_terminal_report(analyzer):
    stats = analyzer.get_basic_stats()
    cats = analyzer.sales_by_category()
    top_p = analyzer.top_products(3)
    
    print("\n" + "="*50)
    print("📊 SALES DATA ANALYSIS REPORT")
    print("="*50)
    print(f"📅 Analysis Period: {stats.get('start_date')} to {stats.get('end_date')}")
    print(f"💰 Total Sales: ${stats['total_sales']:,.2f}")
    print(f"📦 Total Orders: {stats['total_orders']:,}")
    print(f"💳 Average Order Value: ${stats['avg_order_value']:.2f}")
    print(f"👥 Unique Customers: {stats['unique_customers']}")
    
    print("\n🏆 TOP CATEGORIES BY REVENUE:")
    for idx, row in cats.iterrows():
        pct = (row['total_amount'] / stats['total_sales']) * 100
        print(f" - {idx}: ${row['total_amount']:,.2f} ({pct:.1f}%)")
        
    print("\n⭐ TOP 3 PRODUCTS:")
    for idx, row in top_p.iterrows():
        print(f" - {idx}: ${row['total_amount']:,.2f}")
    print("="*50 + "\n")
