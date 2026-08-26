#rapeir_manager.py
# DAY 8: TECH REPAIR MANAGER WITH MODULES

import tech_utils
import datetime
import os

def log_repair(customer, device, issue, parts_cost, labor_hours):
    """Logs a repair with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Use functions from tech_utils
    cost = tech_utils.calculate_repair_cost(device, parts_cost, labor_hours)
    status = tech_utils.device_status(device, 3)  # Assuming 3 years old
    
    record = f"""
    ========================================
    Repair Log - {timestamp}
    Customer: {customer}
    Device: {device}
    Issue: {issue}
    Status Assessment: {status}
    Parts Cost: Nu.{parts_cost}
    Labor Hours: {labor_hours}
    Total Cost: Nu.{cost}
    ========================================
    """
    
    with open("repair_log.txt", "a") as file:
        file.write(record)
    
    print("Repair logged successfully!")
    return cost

def view_repair_log():
    """Displays all repair logs"""
    try:
        if not os.path.exists("repair_log.txt"):
            print("No repair logs found!")
            return
        
        with open("repair_log.txt", "r") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading log: {e}")

def check_inventory():
    """Checks inventory using a file"""
    try:
        if not os.path.exists("inventory.txt"):
            print("No inventory file found. Creating one...")
            with open("inventory.txt", "w") as file:
                file.write("Screens:10\n")
                file.write("Batteries:15\n")
                file.write("Chargers:20\n")
                file.write("Keyboards:8\n")
            print("Default inventory created!")
            return
        
        with open("inventory.txt", "r") as file:
            print("\n===== INVENTORY =====")
            for line in file:
                part, qty = line.strip().split(":")
                print(f"{part}: {qty} available")
    except Exception as e:
        print(f"Inventory error: {e}")

def update_inventory(part, quantity):
    """Updates inventory"""
    try:
        inventory = {}
        if os.path.exists("inventory.txt"):
            with open("inventory.txt", "r") as file:
                for line in file:
                    key, val = line.strip().split(":")
                    inventory[key] = int(val)

        inventory[part] = inventory[part] + quantity if part in inventory else quantity
        with open("inventory.txt", "w") as file:
            for key, val in inventory.items():
                file.write(f"{key}:{val}\n")

        print(f"Inventory updated! {part}: {inventory[part]}")
    except Exception as e:
        print(f"Error updating inventory: {e}")

def main():
    """Main program"""
    print("===== TECH REPAIR MANAGER =====")
    print(f"Date: {datetime.datetime.now().strftime('%B %d, %Y')}")
    
    while True:
        print("\n1. Log a repair")
        print("2. View repair log")
        print("3. Check inventory")
        print("4. Update inventory")
        print("5. Device status check")
        print("6. Battery check")
        print("7. Exit")
        
        try:
            choice = int(input("Enter choice (1-7): "))
            
            if choice == 1:
                customer = input("Customer name: ")
                device = input("Device type (laptop/mobile): ")
                issue = input("Issue description: ")
                parts_cost = float(input("Parts cost: Nu."))
                labor_hours = float(input("Labor hours: "))
                
                total = log_repair(customer, device, issue, parts_cost, labor_hours)
                print(f"Total cost: Nu.{total}")
                
            elif choice == 2:
                view_repair_log()
                
            elif choice == 3:
                check_inventory()
                
            elif choice == 4:
                part = input("Part name: ")
                qty = int(input("Quantity to add: "))
                update_inventory(part, qty)
                
            elif choice == 5:
                device = input("Device type (laptop/mobile): ")
                age = int(input("Age in years: "))
                status = tech_utils.device_status(device, age)
                print(f"Status: {status}")
                
            elif choice == 6:
                level = int(input("Battery level (0-100): "))
                status = tech_utils.check_battery(level)
                print(f"Battery status: {status}")
                
            elif choice == 7:
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Invalid input! Please enter numbers correctly.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()