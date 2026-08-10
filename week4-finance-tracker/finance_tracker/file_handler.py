"""
File Operations: Load, Save, Backup, and Export data.
"""

import json
import csv
import os
import shutil
from datetime import datetime
from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.json")
BACKUP_DIR = os.path.join(DATA_DIR, "backup")
EXPORTS_DIR = os.path.join(DATA_DIR, "exports")

def ensure_directories():
    """Ensure required data directories exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(EXPORTS_DIR, exist_ok=True)

def save_data(manager: ExpenseManager) -> bool:
    """Save expense data and budget to JSON file."""
    ensure_directories()
    payload = {
        "monthly_budget": manager.monthly_budget,
        "expenses": [e.to_dict() for e in manager.expenses]
    }
    try:
        with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)
        return True
    except IOError as e:
        print(f"❌ Error saving data: {e}")
        return False

def load_data(manager: ExpenseManager) -> bool:
    """Load expense data from JSON file."""
    ensure_directories()
    if not os.path.exists(EXPENSES_FILE):
        return False

    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            manager.monthly_budget = data.get("monthly_budget", 0.0)
            manager.expenses = [Expense.from_dict(item) for item in data.get("expenses", [])]
        return True
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️ Error reading dataset: {e}")
        return False

def create_backup() -> bool:
    """Create a timestamped backup of the database."""
    ensure_directories()
    if not os.path.exists(EXPENSES_FILE):
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"expenses_backup_{timestamp}.json")
    try:
        shutil.copy(EXPENSES_FILE, backup_path)
        print(f"✅ Backup created at: {backup_path}")
        return True
    except IOError as e:
        print(f"❌ Backup failed: {e}")
        return False

def export_to_csv(manager: ExpenseManager) -> str:
    """Export expenses to CSV file."""
    ensure_directories()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join(EXPORTS_DIR, f"finance_export_{timestamp}.csv")

    try:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Date", "Category", "Amount", "Description"])
            for e in manager.expenses:
                writer.writerow([e.expense_id, e.date, e.category, e.amount, e.description])
        return csv_path
    except IOError as e:
        print(f"❌ Export failed: {e}")
        return ""
