# DAY 6: REPAIR SHOP MANAGEMENT SYSTEM

def save_repair(customer_name, device_type, issue, status="pending"):
    """Saves a repair record to file"""
    with open("repairs.txt", "a") as file:
        file.write(f"{customer_name}|{device_type}|{issue}|{status}\n")
    print(f"✓ Repair record saved for {customer_name}")

def view_repairs():
    """Shows all repair records"""
    try:
        with open("repairs.txt", "r") as file:
            repairs = file.readlines()
            
        if not repairs:
            print("No repairs in system")
            return
            
        print("\n===== REPAIR RECORDS =====")
        for repair in repairs:
            data = repair.strip().split("|")
            print(f"Customer: {data[0]}")
            print(f"Device: {data[1]}")
            print(f"Issue: {data[2]}")
            print(f"Status: {data[3]}")
            print("-" * 20)
            
    except FileNotFoundError:
        print("No repair records found!")

def search_customer(name):
    """Searches for repair records by customer name"""
    try:
        with open("repairs.txt", "r") as file:
            found = False
            for line in file:
                data = line.strip().split("|")
                if data[0].lower() == name.lower():
                    print(f"Found: {data[0]} - {data[1]} - {data[2]} - {data[3]}")
                    found = True
            if not found:
                print(f"No records found for {name}")
    except FileNotFoundError:
        print("No repair records found!")

def update_status(name, new_status):
    """Updates the status of a repair"""
    try:
        with open("repairs.txt", "r") as file:
            lines = file.readlines()
        
        updated = False
        with open("repairs.txt", "w") as file:
            for line in lines:
                data = line.strip().split("|")
                if data[0].lower() == name.lower():
                    file.write(f"{data[0]}|{data[1]}|{data[2]}|{new_status}\n")
                    updated = True
                    print(f"✓ Status updated to {new_status} for {name}")
                else:
                    file.write(line)
        
        if not updated:
            print(f"Customer {name} not found!")
            
    except FileNotFoundError:
        print("No repair records found!")

def count_by_device():
    """Counts repairs by device type"""
    try:
        with open("repairs.txt", "r") as file:
            counts = {}
            for line in file:
                data = line.strip().split("|")
                device = data[1]
                if device in counts:
                    counts[device] = counts[device] + 1
                else:
                    counts[device] = 1
            
            print("\n===== DEVICE STATISTICS =====")
            for device, count in counts.items():
                print(f"{device}: {count} repairs")
                
    except FileNotFoundError:
        print("No repair records found!")

# MAIN PROGRAM
print("===== REPAIR SHOP MANAGER =====")
while True:
    print("\n1. Add new repair")
    print("2. View all repairs")
    print("3. Search customer")
    print("4. Update status")
    print("5. View device statistics")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        name = input("Customer name: ")
        device = input("Device type (Laptop/Mobile/Tablet): ")
        issue = input("Issue description: ")
        save_repair(name, device, issue)
        
    elif choice == "2":
        view_repairs()
        
    elif choice == "3":
        name = input("Enter customer name: ")
        search_customer(name)
        
    elif choice == "4":
        name = input("Enter customer name: ")
        status = input("New status (pending/in-progress/completed): ")
        update_status(name, status)
        
    elif choice == "5":
        count_by_device()
        
    elif choice == "6":
        print("Goodbye! Happy repairing!")
        break
        
    else:
        print("Invalid choice! Try again.")
