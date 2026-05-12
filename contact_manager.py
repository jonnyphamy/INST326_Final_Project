class Contact:
    """Represents one contact."""

    def __init__(self, name, phone, email, category):
        """Initialize a Contact object."""
        if name == "": # Make sure the name is not blank
            raise ValueError("Name cannot be empty.")
        if phone == "": # Make sure the phone number is not blank
            raise ValueError("Phone cannot be empty.")
        if email == "": # Make sure the email is not blank
            raise ValueError("Email cannot be empty.")
        if category == "": # Make sure the category is not blank
            raise ValueError("Category cannot be empty.")

        # Save the contact information
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def __repr__(self): 
        """returns a representation of the contact"""
        # Return a string that looks like the constructor call
        return (
            f"Contact('{self.name}', '{self.phone}', "
            f"'{self.email}', '{self.category}')"
        )

    def __str__(self):
        """returns a string version of the contact"""
        # Return the contact information in a readable format
        return (
            f"{self.name} | Phone: {self.phone} | "
            f"Email: {self.email} | Category: {self.category}"
        )

    def __eq__(self, other):
        """returns true if the contacts have the same attributes"""
        # Make sure the other object is a Contact
        if not isinstance(other, Contact):
            return NotImplemented
        # Compare all attributes
        return (
            self.name == other.name
            and self.phone == other.phone
            and self.email == other.email
            and self.category == other.category
        )

    def __lt__(self, other):
        """returns true if the contacts name comes before another one"""
        if not isinstance(other, Contact):  # Make sure the other object is a Contact
            return NotImplemented

        return self.name < other.name # Compare the names alphabetically
    
class ContactBook:
    """Represents a collection of Contact objects."""

    def __init__(self, owner):
        """initializes a contactbook object"""
         # Save the owner's name
        self.owner = owner
        self.contacts = [] # Start with an empty list of contacts

    def add_contact(self, contact):
        """adds a contact object to the contact book"""
        if not isinstance(contact, Contact):
            raise ValueError("Only Contact objects can be added.")
        self.contacts.append(contact)

    def get_categories(self):
        """returns a set of unique contact categories"""
        categories = set()

        for contact in self.contacts:
            categories.add(contact.category)

        return categories

    def get_category_counts(self):
        """returns a dictionary counting contacts by their categories using counting pattern"""
        counts = {}

        for contact in self.contacts: 
            counts[contact.category] = counts.get(contact.category, 0) + 1

        return counts

    def search_by_name(self, name):
        matches = [] # Store all matching contacts
        # Check each contact in the contact book
        for contact in self.contacts: # Compare names without worrying about uppercase or lowercase
            if contact.name.lower() == name.lower(): 
                matches.append(contact)

        return matches
     
    def get_contact_records(self):
    
        """Return all contacts as tuples."""
        
        records = [] # Store each contact as a tuple

        for contact in self.contacts: # Convert every contact into a tuple and add it to the list
            records.append(
            (
                contact.name,
                contact.phone,
                contact.email,
                contact.category
            )
        )

        return records
    
    
    def __repr__(self):
        """ returns a representation of the ContactBook object."""
        return f"ContactBook('{self.owner}', {self.contacts})"

    def __str__(self):

        """returns the number of contacts in the contact book"""
        return f"{self.owner}'s Contact Book with {len(self.contacts)} contacts"

    def __len__(self):  
     """Check if a contact exists in the contact book.

        Args:
            contact (Contact): The contact to check.

        Returns:
            bool: True if the contact exists.
        """    
     return len(self.contacts) # Return the length of the contacts list

    def __contains__(self, contact): # Check if the contact exists in the list
        """returns an interator for the contacts list"""
        return contact in self.contacts

    def __iter__(self): # Return an iterator for the contacts list
        return iter(self.contacts)

    def __getitem__(self, index): # Return the contact at the given position
        """Return a contact at a specific index.

        Args:
            index (int): The position of the contact.

        Returns:
            Contact: The contact at the given index.
        """
        return self.contacts[index]

    def __add__(self, other): 
        """
     Combine two ContactBook objects.

        Args:
            other (ContactBook): This is another contact book.

        Returns:
            ContactBook: A new combined contact book.
        """
        
        if not isinstance(other, ContactBook): # Make sure the other object is also a ContactBook
            return NotImplemented
        new_book = ContactBook(self.owner + " and " + other.owner) # Create a new contact book with both owners' names

        for contact in self.contacts: # Add all contacts from the first contact book
            new_book.add_contact(contact)

        for contact in other.contacts:  # Add all contacts from the second contact book
            new_book.add_contact(contact)

        return new_book
if __name__ == "__main__":

    """Run test code for the Contact Manager program."""

    contact1 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")
    contact2 = Contact("Alex Kim", "240-555-2222", "alex@email.com", "work")
    contact3 = Contact("Mia Lee", "443-555-3333", "mia@email.com", "school")
    contact4 = Contact("Jay Pham", "301-555-1111", "jay@email.com", "school")

    book1 = ContactBook("Jonathan")
    book1.add_contact(contact1)
    book1.add_contact(contact2)

    book2 = ContactBook("Friend")
    book2.add_contact(contact3)

    print(book1)
    print()

    print("All contacts:")
    for contact in book1:
        print(contact)

    print()
    print("Number of contacts:", len(book1))

    print()
    print("First contact:", book1[0])

    print()
    print("Categories:", book1.get_categories())

    print()
    print("Category counts:", book1.get_category_counts())

    print()
    print("Search:", book1.search_by_name("Jay Pham"))

    print()
    print("Equality check:", contact1 == contact4)

    print()
    print("Membership:", contact1 in book1)

    print()
    print("Sorted:")
    for contact in sorted(book1):
        print(contact)

    print()
    combined = book1 + book2
    print(combined)

    for contact in combined:
        print(contact) 
