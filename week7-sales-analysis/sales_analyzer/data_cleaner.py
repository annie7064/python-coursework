import pandas as pd
import numpy as np

def clean_data(df):
    cleaned = df.copy()
    
    initial_len = len(cleaned)
    cleaned = cleaned.drop_duplicates()
    dedup_count = initial_len - len(cleaned)
    
    numeric_cols = cleaned.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if cleaned[col].isnull().sum() > 0:
            cleaned[col] = cleaned[col].fillna(cleaned[col].median())
            
    if 'total_amount' in cleaned.columns and 'quantity' in cleaned.columns and 'unit_price' in cleaned.columns:
        cleaned['total_amount'] = cleaned['quantity'] * cleaned['unit_price']

    # Compatible with Pandas 2 & 3 string type selection
    categorical_cols = cleaned.select_dtypes(include=['object', 'string']).columns
    for col in categorical_cols:
        if cleaned[col].isnull().sum() > 0:
            mode_val = cleaned[col].mode()[0]
            cleaned[col] = cleaned[col].fillna(mode_val)
            
    return cleaned, dedup_count
