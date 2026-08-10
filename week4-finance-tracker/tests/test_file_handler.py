import unittest
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker import file_handler

class TestFileHandler(unittest.TestCase):
    def test_save_and_load(self):
        manager = ExpenseManager()
        manager.monthly_budget = 500.0
        self.assertTrue(file_handler.save_data(manager))

if __name__ == "__main__":
    unittest.main()
