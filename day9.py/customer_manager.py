import csv
import os

class CustomerManager:
    def __init__(self):
        self.filename = "customers.csv"
        self.headers = ["id", "name", "phone", "device", "issue", "status"]
    
    def create_file(self):
        """Create CSV file with headers if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
            print("✓ Customer database created!")
    
    def get_next_id(self):
        """Get next customer ID"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers
                rows = list(reader)
                if rows:
                    last_id = int(rows[-1][0])
                    return last_id + 1
                return 1
        except:
            return 1
    
    def add_customer(self, name, phone, device, issue):
        """Add new customer"""
        self.create_file()
        customer_id = self.get_next_id()
        
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([customer_id, name, phone, device, issue, "pending"])
        
        print(f"✓ Customer #{customer_id} added!")
    
    def view_all(self):
        """Show all customers"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                rows = list(reader)
                
                if not rows:
                    print("No customers found!")
                    return
                
                print("\n===== CUSTOMER LIST =====")
                print(f"{headers[0]:<5} {headers[1]:<12} {headers[2]:<12} {headers[3]:<10} {headers[4]:<15} {headers[5]:<10}")
                print("-" * 70)
                
                for row in rows:
                    print(f"{row[0]:<5} {row[1]:<12} {row[2]:<12} {row[3]:<10} {row[4]:<15} {row[5]:<10}")
        except FileNotFoundError:
            print("No database found! Add a customer first.")
    
    def search(self, search_term):
        """Search customers by name or device"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                rows = list(reader)
                
                found = False
                for row in rows:
                    if search_term.lower() in row[1].lower() or search_term.lower() in row[3].lower():
                        print(f"#{row[0]} | {row[1]} | {row[3]} | {row[4]} | {row[5]}")
                        found = True
                
                if not found:
                    print(f"No customers found with '{search_term}'")
        except FileNotFoundError:
            print("No database found!")
    
    def update_status(self, customer_id, new_status):
        """Update customer status"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                rows = list(reader)
            
            updated = False
            for i, row in enumerate(rows):
                if row[0] == str(customer_id):
                    rows[i][5] = new_status
                    updated = True
                    break
            
            if updated:
                with open(self.filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(rows)
                print(f"✓ Customer #{customer_id} status updated to '{new_status}'")
            else:
                print(f"Customer #{customer_id} not found!")
                
        except FileNotFoundError:
            print("No database found!")
    
    def delete(self, customer_id):
        """Delete customer"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                rows = list(reader)
            
            deleted = False
            for i, row in enumerate(rows):
                if row[0] == str(customer_id):
                    del rows[i]
                    deleted = True
                    break
            
            if deleted:
                with open(self.filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    writer.writerows(rows)
                print(f"✓ Customer #{customer_id} deleted!")
            else:
                print(f"Customer #{customer_id} not found!")
                
        except FileNotFoundError:
            print("No database found!")
    
    def count_by_device(self):
        """Count customers by device type"""
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                rows = list(reader)
                
                counts = {}
                for row in rows:
                    device = row[3]
                    counts[device] = counts.get(device, 0) + 1
                
                print("\n===== DEVICE STATS =====")
                for device, count in counts.items():
                    print(f"{device}: {count}")
        except FileNotFoundError:
            print("No database found!")

def main():
    manager = CustomerManager()
    
    while True:
        print("\n===== CUSTOMER MANAGER =====")
        print("1. Add customer")
        print("2. View all")
        print("3. Search")
        print("4. Update status")
        print("5. Delete customer")
        print("6. Device statistics")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ")
        
        if choice == "1":
            name = input("Customer name: ")
            phone = input("Phone number: ")
            device = input("Device (Laptop/Mobile/Tablet): ")
            issue = input("Issue: ")
            manager.add_customer(name, phone, device, issue)
            
        elif choice == "2":
            manager.view_all()
            
        elif choice == "3":
            search = input("Search by name or device: ")
            manager.search(search)
            
        elif choice == "4":
            try:
                cid = int(input("Customer ID: "))
                status = input("New status (pending/in-progress/done): ")
                manager.update_status(cid, status)
            except ValueError:
                print("Invalid ID!")
            
        elif choice == "5":
            try:
                cid = int(input("Customer ID to delete: "))
                confirm = input(f"Delete customer #{cid}? (y/n): ")
                if confirm.lower() == "y":
                    manager.delete(cid)
            except ValueError:
                print("Invalid ID!")
            
        elif choice == "6":
            manager.count_by_device()
            
        elif choice == "7":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()