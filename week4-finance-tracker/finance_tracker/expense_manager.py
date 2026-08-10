"""
Expense Manager for handling collections of expenses and budget management.
"""

from typing import List
from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses: List[Expense] = []
        self.monthly_budget: float = 0.0

    def add_expense(self, expense: Expense):
        """Add a new expense."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> bool:
        """Remove expense by ID."""
        initial_count = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.expense_id != expense_id]
        return len(self.expenses) < initial_count

    def search_expenses(self, term: str) -> List[Expense]:
        """Search expenses by category or description."""
        term_lower = term.lower()
        return [
            e for e in self.expenses
            if term_lower in e.category.lower() or term_lower in e.description.lower()
        ]

    def filter_by_month(self, year_month: str) -> List[Expense]:
        """Filter expenses by YYYY-MM string."""
        return [e for e in self.expenses if e.date.startswith(year_month)]

    def get_total_spending(self) -> float:
        """Calculate total spending."""
        return sum(e.amount for e in self.expenses)
