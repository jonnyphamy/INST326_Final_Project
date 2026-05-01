"""Manage contacts through a command-line address book application."""
import argparse
import json
from pathlib import Path


DEFAULT_DATA_FILE = "contacts.json"


class Contact:
    """Represent one contact in the address book.

    Attributes:
        name (str): Contact's full name.
        phone (str): Contact's phone number.
        email (str): Contact's email address.
        category (str): Contact category such as friend, school, or work.
        favorite (bool): True when the contact is marked as a favorite.
    """

    def __init__(self, name, phone, email, category="general",
                 favorite=False):
        """Initialize a Contact object.

        Args:
            name (str): Contact's full name.
            phone (str): Contact's phone number.
            email (str): Contact's email address.
            category (str): Contact category label.
            favorite (bool): Whether the contact is a favorite.
        """
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()
        self.category = category.strip().lower()
        self.favorite = favorite

    def matches_keyword(self, keyword):
        """Return whether a keyword appears in the contact data.

        Args:
            keyword (str): Search term provided by the user.

        Returns:
            bool: True if the keyword appears in the name, phone, email,
                or category.
        """
        normalized_keyword = keyword.strip().lower()
        return normalized_keyword in self.name.lower() \
            or normalized_keyword in self.phone.lower() \
            or normalized_keyword in self.email.lower() \
            or normalized_keyword in self.category.lower()
