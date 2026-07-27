"""
Unit tests for Contact Management System.
"""

import unittest
from contacts_manager import validate_phone, validate_email, search_contacts

class TestContactManager(unittest.TestCase):

    def test_phone_validation_valid(self):
        valid_phones = ["+1 (234) 567-8900", "1234567890", "+919876543210"]
        for p in valid_phones:
            is_valid, cleaned = validate_phone(p)
            self.assertTrue(is_valid)

    def test_phone_validation_invalid(self):
        invalid_phones = ["1234", "abc1234567", "000"]
        for p in invalid_phones:
            is_valid, _ = validate_phone(p)
            self.assertFalse(is_valid)

    def test_email_validation(self):
        self.assertTrue(validate_email("john@example.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_search_partial_match(self):
        test_contacts = {
            "Alice Smith": {"phone": "1234567890", "group": "Work"},
            "Bob Jones": {"phone": "0987654321", "group": "Friends"}
        }
        results = search_contacts(test_contacts, "alice")
        self.assertIn("Alice Smith", results)

if __name__ == "__main__":
    unittest.main()
