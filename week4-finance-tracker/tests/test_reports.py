import unittest
from finance_tracker.expense import Expense
from finance_tracker.reports import generate_monthly_report

class TestReports(unittest.TestCase):
    def test_report_execution(self):
        expenses = [Expense(50, "Bills", "Electricity", "2026-03-15")]
        # Ensure function executes without raising exceptions
        generate_monthly_report(expenses, "2026-03", 200.0)

if __name__ == "__main__":
    unittest.main()
