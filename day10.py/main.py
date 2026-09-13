# main.py - Menu and user input only

from customer_manager import CustomerManager


def show_menu():
    print("\n===== CUSTOMER MANAGER =====")
    print("1. Add customer")
    print("2. View all")
    print("3. Search by name/device")
    print("4. Update status")
    print("5. Delete customer")
    print("6. Device statistics")
    print("7. Export to text file")
    print("8. Pending count")
    print("9. Find by phone")
    print("10. Clear all")
    print("11. Exit")


def main():
    manager = CustomerManager()

    while True:
        show_menu()
        choice = input("Enter choice (1-11): ")

        if choice == "1":
            name = input("Customer name: ")
            phone = input("Phone number: ")
            device = input("Device: ")
            issue = input("Issue: ")
            manager.add_customer(name, phone, device, issue)

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            term = input("Search: ")
            manager.search(term)

        elif choice == "4":
            try:
                cid = int(input("Customer ID: "))
                status = input("New status: ")
                manager.update_status(cid, status)
            except ValueError:
                print("Invalid ID!")

        elif choice == "5":
            try:
                cid = int(input("Customer ID to delete: "))
                confirm = input(f"Delete #{cid}? (y/n): ")
                if confirm.lower() == "y":
                    manager.delete(cid)
            except ValueError:
                print("Invalid ID!")

        elif choice == "6":
            manager.count_by_device()

        elif choice == "7":
            manager.export_to_text()

        elif choice == "8":
            manager.get_pending_count()

        elif choice == "9":
            phone = input("Phone number: ")
            manager.find_by_phone(phone)

        elif choice == "10":
            manager.clear_all()

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
