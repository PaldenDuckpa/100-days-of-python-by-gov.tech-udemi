

def safe_int_input(prompt):
    """Safely gets integer input from user"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def safe_float_input(prompt):
    """Safely gets float input from user"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def diagnose_laptop():
    """Diagnoses laptop issues"""
    print("\n===== LAPTOP DIAGNOSTIC =====")
    try:
        battery_level = safe_int_input("Battery level (0-100): ")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Battery must be between 0 and 100!")
        
        screen = input("Is screen working? (yes/no): ").lower()
        if screen not in ["yes", "no"]:
            raise ValueError("Please enter yes or no!")
        
        if battery_level < 10:
            print(" Critical battery - needs charging!")
        if screen == "no":
            print(" Screen replacement needed!")
        if battery_level < 50 and screen == "yes":
            print(" Battery needs calibration")
        if battery_level > 80 and screen == "yes":
            print(" System appears healthy")
            
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Diagnostic error: {e}")
    
    print("Diagnostic complete!")

def diagnose_mobile():
    """Diagnoses mobile issues"""
    print("\n===== MOBILE DIAGNOSTIC =====")
    try:
        storage = safe_int_input("Storage used (GB): ")
        if storage < 0:
            raise ValueError("Storage cannot be negative!")
        
        apps = safe_int_input("Number of apps: ")
        if apps < 0:
            raise ValueError("Apps cannot be negative!")
        
        if storage > 50:
            print(" Storage almost full - needs cleanup")
        if apps > 50:
            print(" Too many apps - suggest removal")
        if storage < 20 and apps < 20:
            print(" System is running smoothly")
            
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Diagnostic error: {e}")
    
    print("Diagnostic complete!")

def repair_system():
    """Main repair system with error handling"""
    print("===== TECH REPAIR DIAGNOSTIC SYSTEM =====")
    
    while True:
        print("\n1. Laptop Diagnostic")
        print("2. Mobile Diagnostic")
        print("3. Exit")
        
        try:
            choice = safe_int_input("Enter your choice (1-3): ")
            
            if choice == 1:
                diagnose_laptop()
            elif choice == 2:
                diagnose_mobile()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\nExiting safely...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.")

# Run the system
if __name__ == "__main__":
    try:
        repair_system()
    except Exception as e:
        print(f"System error: {e}")
        print("Please restart the program.")bin/python3

print("give me a bottle of rum!")
