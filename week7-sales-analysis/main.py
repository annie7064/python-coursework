from sales_analyzer import (
    load_sales_data,
    clean_data,
    SalesAnalyzer,
    create_visualizations,
    export_excel_report,
    print_terminal_report
)

def main():
    raw_file = "data/raw/sales_data.csv"
    processed_file = "data/processed/cleaned_sales_data.csv"
    
    print("1. Loading raw dataset...")
    df_raw = load_sales_data(raw_file)
    
    print("2. Cleaning dataset...")
    df_clean, removed = clean_data(df_raw)
    print(f"   Removed {removed} duplicates. Cleaned missing values.")
    
    df_clean.to_csv(processed_file, index=False)
    
    print("3. Analyzing metrics...")
    analyzer = SalesAnalyzer(df_clean)
    
    print("4. Generating visual charts...")
    create_visualizations(analyzer)
    
    print("5. Exporting Excel report...")
    export_excel_report(analyzer)
    
    print_terminal_report(analyzer)

if __name__ == "__main__":
    main()
