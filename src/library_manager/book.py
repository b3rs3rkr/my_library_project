# src/library_manager/book.py

class Book:
    """Represents a single book in a library."""

    def __init__(self, title: str, author: str, isbn: str):
        """
        Initializes a new Book object.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The International Standard Book Number.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_read = False

    def mark_as_read(self):
        """Marks the book as read."""
        self.is_read = True
        print(f"Book '{self.title}' marked as read.")

    def mark_as_unread(self):
        """Marks the book as unread."""
        self.is_read = False
        print(f"Book '{self.title}' marked as unread.")

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the book.
        """
        status = "Read" if self.is_read else "Unread"
        return f"'{self.title}' by '{self.author}' (ISBN: {self.isbn}) - Status: {status}"
    
    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the object.
        """
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"