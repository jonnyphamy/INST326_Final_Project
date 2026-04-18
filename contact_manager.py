import pytest
from contact_manager import (
    Contact,
    AddressBook,
    convert_favorite_choice,
    format_contacts,
)


def test_contact_stores_attributes():
    """Test that a Contact stores the correct attribute values."""
    contact = Contact("Kyle Do", "301-555-1234", "kyle@example.com")

    assert contact.name == "Kyle Do"
    assert contact.phone == "301-555-1234"
    assert contact.email == "kyle@example.com"
    assert contact.category == "general"
    assert contact.favorite is False
