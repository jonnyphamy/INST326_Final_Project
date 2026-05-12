"""Tests for contact_manager.py."""

# Import the classes we want to test
from contact_manager import Contact, ContactBook


def test_contact_attributes():
    """Make sure a Contact stores all attribute values correctly."""

    # Create a sample contact
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    # Check each attribute
    assert contact.name == "Jay Pham"
    assert contact.phone == "301-555-1111"
    assert contact.email == "jay@email.com"
    assert contact.category == "school"


def test_contact_equality():
    """Check that two identical contacts are considered equal."""

    # Create two contacts with the same information
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    # They should be equal
    assert contact1 == contact2


def test_contact_less_than():
    """Check that contacts are compared alphabetically by name."""

    # Alex should come before Jay
    contact1 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    contact2 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert contact1 < contact2


def test_contact_repr():
    """Check the __repr__ output."""

    # Create a contact
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    # Verify the exact repr string
    assert repr(contact) == (
        "Contact('Jay Pham', '301-555-1111', "
        "'jay@email.com', 'school')"
    )


def test_contact_str():
    """Check the __str__ output."""

    # Create a contact
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    # Verify the formatted string
    assert str(contact) == (
        "Jay Pham | Phone: 301-555-1111 | "
        "Email: jay@email.com | Category: school"
    )


def test_contact_empty_name_raises_error():
    """Make sure an empty name raises ValueError."""

    try:
        Contact("", "301", "jay@email.com", "school")
        assert False  # Should not reach this line
    except ValueError:
        assert True


def test_contact_empty_phone_raises_error():
    """Make sure an empty phone number raises ValueError."""

    try:
        Contact("Jay Pham", "", "jay@email.com", "school")
        assert False
    except ValueError:
        assert True


def test_contact_empty_email_raises_error():
    """Make sure an empty email raises ValueError."""

    try:
        Contact("Jay Pham", "301", "", "school")
        assert False
    except ValueError:
        assert True


def test_contact_book_add_contact_and_len():
    """Check that add_contact works and updates the length."""

    # Create a contact and contact book
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    # Add the contact
    book.add_contact(contact)

    # Length should now be 1
    assert len(book) == 1


def test_contact_book_contains():
    """Check that 'in' works with the contact book."""

    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    # The contact should be found in the book
    assert contact in book


def test_contact_book_indexing():
    """Check that contacts can be accessed by index."""

    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    # The first contact should be the one we added
    assert book[0] == contact


def test_contact_book_iteration():
    """Check that we can loop through the contact book."""

    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    book = ContactBook("Jonathan")

    # Add two contacts
    book.add_contact(contact1)
    book.add_contact(contact2)

    # Store all names found while looping
    names = []

    for contact in book:
        names.append(contact.name)

    assert names == ["Jay Pham", "Alex Kim"]


def test_contact_book_categories():
    """Check that get_categories returns unique categories."""

    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    book = ContactBook("Jonathan")

    book.add_contact(contact1)
    book.add_contact(contact2)

    assert book.get_categories() == {"school", "work"}


def test_contact_book_category_counts():
    """Check that get_category_counts counts categories correctly."""

    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    contact3 = Contact("Mia Lee", "443-555-3333", "mia@email.com", "school")
    book = ContactBook("Jonathan")

    # Add all contacts
    book.add_contact(contact1)
    book.add_contact(contact2)
    book.add_contact(contact3)

    # School appears twice, work appears once
    assert book.get_category_counts() == {"school": 2, "work": 1}


def test_contact_book_search_by_name():
    """Check that search_by_name works and ignores case."""

    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    # Search should work with exact and lowercase names
    assert book.search_by_name("Jay Pham") == [contact]
    assert book.search_by_name("jay pham") == [contact]

    # Searching for a missing contact should return an empty list
    assert book.search_by_name("Missing") == []


def test_contact_book_records():
    """Check that get_contact_records returns tuples."""

    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert book.get_contact_records() == [
        ("Jay Pham", "301-555-1111", "jay@email.com", "school")
    ]


def test_contact_book_add():
    """Check that two contact books can be combined with +."""

    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Mia Lee", "443-555-3333", "mia@email.com", "school")

    book1 = ContactBook("Jonathan")
    book2 = ContactBook("Friend")

    # Add one contact to each book
    book1.add_contact(contact1)
    book2.add_contact(contact2)

    # Combine the books
    combined_book = book1 + book2

    # The new book should contain both contacts
    assert len(combined_book) == 2
    assert contact1 in combined_book
    assert contact2 in combined_book


def test_add_non_contact_raises_error():
    """Make sure adding something other than a Contact raises ValueError."""

    book = ContactBook("Jonathan")

    try:
        # Try to add a string instead of a Contact object
        book.add_contact("not a contact")
        assert False
    except ValueError:
        assert True
