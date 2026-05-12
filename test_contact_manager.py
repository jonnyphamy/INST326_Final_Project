"""Tests for contact_manager.py."""


from contact_manager import Contact, ContactBook


def test_contact_attributes():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert contact.name == "Jay Pham"
    assert contact.phone == "301-555-1111"
    assert contact.email == "jay@email.com"
    assert contact.category == "school"


def test_contact_equality():
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert contact1 == contact2


def test_contact_less_than():
    contact1 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    contact2 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert contact1 < contact2


def test_contact_repr():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert repr(contact) == (
        "Contact('Jay Pham', '301-555-1111', "
        "'jay@email.com', 'school')"
    )


def test_contact_str():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    assert str(contact) == (
        "Jay Pham | Phone: 301-555-1111 | "
        "Email: jay@email.com | Category: school"
    )


def test_contact_empty_name_raises_error():
    try:
        Contact("", "301", "jay@email.com", "school")
        assert False
    except ValueError:
        assert True


def test_contact_empty_phone_raises_error():
    try:
        Contact("Jay Pham", "", "jay@email.com", "school")
        assert False
    except ValueError:
        assert True


def test_contact_empty_email_raises_error():
    try:
        Contact("Jay Pham", "301", "", "school")
        assert False
    except ValueError:
        assert True


def test_contact_book_add_contact_and_len():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert len(book) == 1


def test_contact_book_contains():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert contact in book


def test_contact_book_indexing():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert book[0] == contact


def test_contact_book_iteration():
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    book = ContactBook("Jonathan")

    book.add_contact(contact1)
    book.add_contact(contact2)

    names = []

    for contact in book:
        names.append(contact.name)

    assert names == ["Jay Pham", "Alex Kim"]


def test_contact_book_categories():
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    book = ContactBook("Jonathan")

    book.add_contact(contact1)
    book.add_contact(contact2)

    assert book.get_categories() == {"school", "work"}


def test_contact_book_category_counts():
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    contact3 = Contact("Mia Lee", "443-555-3333", "mia@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact1)
    book.add_contact(contact2)
    book.add_contact(contact3)

    assert book.get_category_counts() == {"school": 2, "work": 1}


def test_contact_book_search_by_name():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert book.search_by_name("Jay Pham") == [contact]
    assert book.search_by_name("jay pham") == [contact]
    assert book.search_by_name("Missing") == []


def test_contact_book_records():
    contact = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    book = ContactBook("Jonathan")

    book.add_contact(contact)

    assert book.get_contact_records() == [
        ("Jay Pham", "301-555-1111", "jay@email.com", "school")
    ]


def test_contact_book_add():
    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Mia Lee", "443-555-3333", "mia@email.com", "school")

    book1 = ContactBook("Jonathan")
    book2 = ContactBook("Friend")

    book1.add_contact(contact1)
    book2.add_contact(contact2)

    combined_book = book1 + book2

    assert len(combined_book) == 2
    assert contact1 in combined_book
    assert contact2 in combined_book


def test_add_non_contact_raises_error():
    book = ContactBook("Jonathan")

    try:
        book.add_contact("not a contact")
        assert False
    except ValueError:
        assert True