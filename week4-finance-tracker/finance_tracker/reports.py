"""
Reporting module for statistics and text visualizations.
"""

from typing import List
from finance_tracker.expense import Expense
from finance_tracker.utils import format_currency

def generate_monthly_report(expenses: List[Expense], year_month: str, budget: float):
    """Generate and display monthly summary report."""
    monthly_expenses = [e for e in expenses if e.date.startswith(year_month)]
    total = sum(e.amount for e in monthly_expenses)

    print(f"\n--- MONTHLY REPORT FOR {year_month} ---")
    print(f"Total Transactions : {len(monthly_expenses)}")
    print(f"Total Spending     : {format_currency(total)}")
    if budget > 0:
        remaining = budget - total
        status = "Under Budget" if remaining >= 0 else "OVER BUDGET!"
        print(f"Monthly Budget     : {format_currency(budget)}")
        print(f"Remaining          : {format_currency(remaining)} ({status})")

def generate_category_breakdown(expenses: List[Expense]):
    """Generate text-based visualization of category spending."""
    if not expenses:
        print("\nNo expense records available.")
        return

    breakdown = {}
    total_spending = sum(e.amount for e in expenses)

    for e in expenses:
        breakdown[e.category] = breakdown.get(e.category, 0.0) + e.amount

    print("\n--- CATEGORY BREAKDOWN ---")
    for category, amount in breakdown.items():
        percentage = (amount / total_spending) * 100 if total_spending > 0 else 0
        bars = "█" * int(percentage // 5)
        print(f"{category:<15} | {format_currency(amount):<10} | {percentage:5.1f}% {bars}")
