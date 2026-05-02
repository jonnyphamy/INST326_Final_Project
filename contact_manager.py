class Contact:
    """Represents one contact."""

    def __init__(self, name, phone, email, category):
        """Initialize a Contact object."""
        if name == "":
            raise ValueError("Name cannot be empty.")
        if phone == "":
            raise ValueError("Phone cannot be empty.")
        if email == "":
            raise ValueError("Email cannot be empty.")
        if category == "":
            raise ValueError("Category cannot be empty.")

        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def __repr__(self):
        return (
            f"Contact('{self.name}', '{self.phone}', "
            f"'{self.email}', '{self.category}')"
        )

    def __str__(self):
        return (
            f"{self.name} | Phone: {self.phone} | "
            f"Email: {self.email} | Category: {self.category}"
        )

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return NotImplemented

        return (
            self.name == other.name
            and self.phone == other.phone
            and self.email == other.email
            and self.category == other.category
        )

    def __lt__(self, other):
        if not isinstance(other, Contact):
            return NotImplemented

        return self.name < other.name
    class ContactBook:
    """Represents a collection of Contact objects."""

    def __init__(self, owner):
        self.owner = owner
        self.contacts = []

    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise ValueError("Only Contact objects can be added.")
        self.contacts.append(contact)

    def get_categories(self):
        categories = set()

        for contact in self.contacts:
            categories.add(contact.category)

        return categories

    def get_category_counts(self):
        counts = {}

        for contact in self.contacts:
            counts[contact.category] = counts.get(contact.category, 0) + 1

        return counts

    def search_by_name(self, name):
        matches = []

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                matches.append(contact)

        return matches
