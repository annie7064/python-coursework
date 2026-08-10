"""
Utility functions for data validation and formatting.
"""

import re
from datetime import datetime

VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Healthcare", "Other"]

def validate_date(date_str: str) -> bool:
    """Validate if date string matches YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount_str: str):
    """Validate and convert amount to float."""
    try:
        val = float(amount_str)
        if val > 0:
            return True, round(val, 2)
        return False, None
    except ValueError:
        return False, None

def format_currency(amount: float) -> str:
    """Format float as currency representation."""
    return f"${amount:,.2f}"
