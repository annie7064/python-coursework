"""
Expense model representation.
"""

import uuid
from datetime import datetime

class Expense:
    def __init__(self, amount: float, category: str, description: str, date: str = None, expense_id: str = None):
        self.expense_id = expense_id if expense_id else str(uuid.uuid4())[:8]
        self.amount = float(amount)
        self.category = category.title()
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> dict:
        """Convert expense instance to dictionary."""
        return {
            "expense_id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create Expense instance from dictionary."""
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"],
            expense_id=data.get("expense_id")
        )
