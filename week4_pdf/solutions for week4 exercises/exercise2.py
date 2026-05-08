class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Title: {self.title}, Author: {self.author}"


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title, author)


class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.issue_frequency = issue_frequency

    def display(self):
        return f"{super().display()}, Issue Frequency: {self.issue_frequency}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_items(self):
        for item in self.items:
            print(item.display())


# Test Cases
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_item(book1)
library.add_item(book2)

# Adding magazines
magazine1 = Magazine("National Geographic", "Multiple Authors", "Monthly")
magazine2 = Magazine("The Economist", "Multiple Authors", "Weekly")
library.add_item(magazine1)
library.add_item(magazine2)

# Display all library items
print("Displaying all library items:")
library.display_items()

# Removing a book
print("\nRemoving a book...")
library.remove_item(book1)

# Display all library items
print("\nDisplaying all library items after removal:")
library.display_items()
