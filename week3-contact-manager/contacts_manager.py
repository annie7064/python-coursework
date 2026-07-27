# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime
import csv

def validate_phone(phone):
    """Validate phone number format"""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    
    # Check if we have 10-15 digits (international format)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_contact(contacts):
    """Add a new contact to the dictionary"""
    print("\n--- ADD NEW CONTACT ---")
    
    # Get contact name
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update instead? (y/n): ").lower()
                if choice == 'y':
                    update_contact(contacts, name)
                    return contacts
            break
        print("Name cannot be empty!")
    
    # Get phone number with validation
    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid:
            break
        print("Invalid phone number! Please enter 10-15 digits.")
    
    # Get email with validation
    while True:
        email = input("Enter email (optional, press Enter to skip): ").strip()
        if not email or validate_email(email):
            break
        print("Invalid email format!")
    
    # Get additional info
    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"
    
    # Store in dictionary
    contacts[name] = {
        'phone': cleaned_phone,
        'email': email if email else None,
        'address': address if address else None,
        'group': group,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    print(f"✅ Contact '{name}' added successfully!")
    return contacts

def search_contacts(contacts, search_term):
    """Search contacts by name (partial match)"""
    search_term = search_term.lower()
    results = {}
    
    for name, info in contacts.items():
        if search_term in name.lower():
            results[name] = info
    
    return results

def display_search_results(results):
    """Display search results in formatted way"""
    if not results:
        print("No contacts found.")
        return
    
    print(f"\nFound {len(results)} contact(s):")
    print("-" * 50)
    
    for i, (name, info) in enumerate(results.items(), 1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        if info['email']:
            print(f"   📧 Email: {info['email']}")
        if info['address']:
            print(f"   📍 Address: {info['address']}")
        print(f"   👥 Group: {info['group']}")
        print()
