import unittest
from finance_tracker.expense import Expense

class TestExpense(unittest.TestCase):
    def test_expense_creation(self):
        e = Expense(25.50, "Food", "Lunch", "2026-03-30")
        self.assertEqual(e.amount, 25.50)
        self.assertEqual(e.category, "Food")
        self.assertEqual(e.to_dict()["description"], "Lunch")

if __name__ == "__main__":
    unittest.main()
