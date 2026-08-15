# DAY 4: DELIVERY MANAGEMENT SYSTEM

print("===== DELIVERY MANAGEMENT SYSTEM =====")

# Master list to store all deliveries
all_deliveries = []

# Get number of deliveries
num = int(input("How many deliveries today? "))

# Collect delivery data using dictionary
for i in range(num):
    print(f"\n--- Delivery #{i+1} ---")
    customer_name = input("Customer name: ")
    address = input("Address: ")
    package_weight = float(input("Package weight (kg): "))
    
    # Create dictionary for this delivery
    delivery = {
        "customer": customer_name,
        "address": address,
        "weight": package_weight,
        "status": "pending"
    }
    
    # Add to master list
    all_deliveries.append(delivery)

# Display all deliveries
print("\n===== ALL DELIVERIES =====")
for delivery in all_deliveries:
    print(f"Customer: {delivery['customer']}")
    print(f"Address: {delivery['address']}")
    print(f"Weight: {delivery['weight']}kg")
    print(f"Status: {delivery['status']}")
    print("---")

# Calculate total weight
total_weight = 0
for delivery in all_deliveries:
    total_weight = total_weight + delivery["weight"]

print(f"\nTotal weight for today: {total_weight}kg")

# Check for heavy packages
print("\nHeavy packages (>20kg):")
for delivery in all_deliveries:
    if delivery["weight"] > 20:
        print(f"- {delivery['customer']}: {delivery['weight']}kg")
