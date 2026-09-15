import json
import os
from datetime import datetime


# ==========================================
# 1. BASE CLASS (Inheritance & Polymorphism)
# ==========================================
class LibraryItem:
    """Base class representing any item in the library."""

    def __init__(self, item_id: str, title: str, author_or_creator: str):
        self.item_id = item_id
        self.title = title
        self.author_or_creator = author_or_creator
        self.is_checked_out = False

    def check_out(self) -> bool:
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_item(self) -> bool:
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def calculate_late_fee(self, days_overdue: int) -> float:
        """Polymorphic method to be overridden by subclasses."""
        return days_overdue * 0.50  # Base rate: $0.50/day

    def to_dict(self) -> dict:
        """Serialize instance to dictionary for JSON saving."""
        return {
            "type": self.__class__.__name__,
            "item_id": self.item_id,
            "title": self.title,
            "author_or_creator": self.author_or_creator,
            "is_checked_out": self.is_checked_out,
        }

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"[{self.item_id}] {self.title} by {self.author_or_creator} ({status})"


# ==========================================
# 2. SUBCLASSES (Inheritance & Method Overriding)
# ==========================================
class Book(LibraryItem):

    def __init__(
        self,
        item_id: str,
        title: str,
        author: str,
        num_pages: int,
        genre: str = "General",
    ):
        super().__init__(item_id, title, author)
        self.num_pages = num_pages
        self.genre = genre

    def calculate_late_fee(self, days_overdue: int) -> float:
        # Books charge $0.25 per day overdue
        return days_overdue * 0.25

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"num_pages": self.num_pages, "genre": self.genre})
        return data


class DVD(LibraryItem):

    def __init__(
        self, item_id: str, title: str, director: str, runtime_minutes: int
    ):
        super().__init__(item_id, title, director)
        self.runtime_minutes = runtime_minutes

    def calculate_late_fee(self, days_overdue: int) -> float:
        # DVDs have higher late fees: $1.00 per day
        return days_overdue * 1.00

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"runtime_minutes": self.runtime_minutes})
        return data


# ==========================================
# 3. USER CLASS (Encapsulation)
# ==========================================
class Member:
    """Represents a library member who can borrow items."""

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []  # List of LibraryItem objects

    def borrow_item(self, item: LibraryItem) -> bool:
        if item.check_out():
            self.borrowed_items.append(item)
            return True
        return False

    def return_item(self, item: LibraryItem) -> bool:
        if item in self.borrowed_items and item.return_item():
            self.borrowed_items.remove(item)
            return True
        return False

    def to_dict(self) -> dict:
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_items": [item.item_id for item in self.borrowed_items],
        }

    def __str__(self):
        return (
            f"Member: {self.name} (ID: {self.member_id}) | "
            f"Borrowed Items: {len(self.borrowed_items)}"
        )


# ==========================================
# 4. SYSTEM MANAGER CLASS (Composition & Storage)
# ==========================================
class LibrarySystem:
    """Manages collection of items and members, plus data persistence."""

    def __init__(self, storage_file: str = "library_data.json"):
        self.storage_file = storage_file
        self.catalog = {}  # item_id -> LibraryItem object
        self.members = {}  # member_id -> Member object
        self.load_data()

    def add_item(self, item: LibraryItem):
        if item.item_id in self.catalog:
            print(f"Error: Item ID {item.item_id} already exists.")
        else:
            self.catalog[item.item_id] = item
            print(f"Added: {item.title}")

    def register_member(self, member: Member):
        if member.member_id in self.members:
            print(f"Error: Member ID {member.member_id} already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Registered member: {member.name}")

    def checkout_item(self, member_id: str, item_id: str):
        member = self.members.get(member_id)
        item = self.catalog.get(item_id)

        if not member:
            print("Error: Member not found.")
            return
        if not item:
            print("Error: Item not found.")
            return

        if item.is_checked_out:
            print(f"Sorry, '{item.title}' is currently checked out.")
        else:
            member.borrow_item(item)
            print(f"Success! '{item.title}' checked out to {member.name}.")

    def return_item(self, member_id: str, item_id: str, days_overdue: int = 0):
        member = self.members.get(member_id)
        item = self.catalog.get(item_id)

        if member and item and item in member.borrowed_items:
            member.return_item(item)
            fee = item.calculate_late_fee(days_overdue)
            print(f"Success! '{item.title}' returned by {member.name}.")
            if fee > 0:
                print(f"Overdue Fee Due: ${fee:.2f}")
        else:
            print("Error: Transaction record invalid.")

    def display_catalog(self):
        print("\n--- Current Library Catalog ---")
        if not self.catalog:
            print("No items in catalog.")
        for item in self.catalog.values():
            print(item)
        print("-------------------------------\n")

    # --- Data Persistence (File I/O) ---
    def save_data(self):
        data = {
            "catalog": [item.to_dict() for item in self.catalog.values()],
            "members": [m.to_dict() for m in self.members.values()],
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)
        print("System state saved successfully.")

    def load_data(self):
        if not os.path.exists(self.storage_file):
            return

        with open(self.storage_file, "r") as f:
            data = json.load(f)

        # Restore Catalog
        for item_data in data.get("catalog", []):
            item_type = item_data.pop("type")
            if item_type == "Book":
                item = Book(**item_data)
            elif item_type == "DVD":
                item = DVD(**item_data)
            else:
                item = LibraryItem(**item_data)
            self.catalog[item.item_id] = item

        # Restore Members
        for m_data in data.get("members", []):
            borrowed_ids = m_data.pop("borrowed_items", [])
            member = Member(**m_data)
            for b_id in borrowed_ids:
                if b_id in self.catalog:
                    item = self.catalog[b_id]
                    member.borrowed_items.append(item)
                    item.is_checked_out = True
            self.members[member.member_id] = member


# ==========================================
# 5. CLI INTERFACE (Procedural Driver)
# ==========================================
def main():
    system = LibrarySystem()

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. Add DVD")
        print("3. Register Member")
        print("4. Check Out Item")
        print("5. Return Item")
        print("6. View Catalog")
        print("7. Save & Exit")

        choice = input("Enter choice (1-7): ").strip()

        try:
            if choice == "1":
                i_id = input("Item ID: ")
                title = input("Title: ")
                author = input("Author: ")
                pages = int(input("Page Count: "))
                genre = input("Genre: ")
                system.add_item(Book(i_id, title, author, pages, genre))

            elif choice == "2":
                i_id = input("Item ID: ")
                title = input("Title: ")
                director = input("Director: ")
                runtime = int(input("Runtime (mins): "))
                system.add_item(DVD(i_id, title, director, runtime))

            elif choice == "3":
                m_id = input("Member ID: ")
                name = input("Member Name: ")
                system.register_member(Member(m_id, name))

            elif choice == "4":
                m_id = input("Member ID: ")
                i_id = input("Item ID to checkout: ")
                system.checkout_item(m_id, i_id)

            elif choice == "5":
                m_id = input("Member ID: ")
                i_id = input("Item ID to return: ")
                overdue = int(input("Days overdue (0 if on time): "))
                system.return_item(m_id, i_id, overdue)

            elif choice == "6":
                system.display_catalog()

            elif choice == "7":
                system.save_data()
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

        except ValueError as e:
            print(f"Input Error: Please enter valid numbers where requested. ({e})")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()