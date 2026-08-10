"""
Entry point driver script.
"""

from finance_tracker.main import FinanceTracker

def main():
    tracker = FinanceTracker()
    tracker.run()

if __name__ == "__main__":
    main()
