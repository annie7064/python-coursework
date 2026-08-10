"""
Main application interface.
"""

from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.utils import VALID_CATEGORIES, validate_amount, validate_date, format_currency
from finance_tracker import file_handler, reports

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        file_handler.load_data(self.manager)

    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)
        
        while True:
            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")
            print("=" * 40)
            
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.search_expenses()
            elif choice == '4':
                self.generate_monthly_report()
            elif choice == '5':
                self.view_category_breakdown()
            elif choice == '6':
                self.set_budget()
            elif choice == '7':
                self.export_data()
            elif choice == '8':
                self.view_statistics()
            elif choice == '9':
                self.backup_restore()
            elif choice == '0':
                file_handler.save_data(self.manager)
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                break
            else:
                print("Invalid choice! Please enter 0-9.")

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        while True:
            amt_str = input("Enter amount: ").strip()
            is_valid, amount = validate_amount(amt_str)
            if is_valid:
                break
            print("Invalid amount! Enter a positive numeric value.")

        print("Categories:", ", ".join(VALID_CATEGORIES))
        category = input("Enter category: ").strip().title()
        if category not in VALID_CATEGORIES:
            category = "Other"

        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date and not validate_date(date):
            print("Invalid date format. Using today's date.")
            date = None

        exp = Expense(amount, category, description, date)
        self.manager.add_expense(exp)
        file_handler.save_data(self.manager)
        print("✅ Expense added successfully!")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.expenses:
            print("No expenses recorded yet.")
            return

        print(f"{'ID':<10} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 65)
        for e in self.manager.expenses:
            print(f"{e.expense_id:<10} {e.date:<12} {e.category:<15} {format_currency(e.amount):<10} {e.description}")

    def search_expenses(self):
        term = input("\nEnter search term (category/description): ").strip()
        results = self.manager.search_expenses(term)
        if not results:
            print("No matching expenses found.")
            return

        print(f"\nFound {len(results)} matching expense(s):")
        for e in results:
            print(f"• [{e.date}] {e.category} - {format_currency(e.amount)} ({e.description})")

    def generate_monthly_report(self):
        ym = input("\nEnter Year-Month (YYYY-MM): ").strip()
        reports.generate_monthly_report(self.manager.expenses, ym, self.manager.monthly_budget)

    def view_category_breakdown(self):
        reports.generate_category_breakdown(self.manager.expenses)

    def set_budget(self):
        b_str = input("\nEnter monthly budget amount: ").strip()
        is_valid, budget = validate_amount(b_str)
        if is_valid:
            self.manager.monthly_budget = budget
            file_handler.save_data(self.manager)
            print(f"✅ Monthly budget set to {format_currency(budget)}")
        else:
            print("Invalid budget amount!")

    def export_data(self):
        csv_path = file_handler.export_to_csv(self.manager)
        if csv_path:
            print(f"✅ Data exported successfully to {csv_path}")

    def view_statistics(self):
        print("\n--- STATISTICS ---")
        total = self.manager.get_total_spending()
        count = len(self.manager.expenses)
        avg = total / count if count > 0 else 0
        print(f"Total Recorded Expenses : {count}")
        print(f"Total Cumulative Spend  : {format_currency(total)}")
        print(f"Average Expense Amount  : {format_currency(avg)}")

    def backup_restore(self):
        if file_handler.create_backup():
            print("✅ Backup completed.")
