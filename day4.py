# lists []

#creat your list 
22				
29	
# Creating lists
deliveries = ["House 12", "Shop 45", "Office 8"]
print(deliveries[0])  # First item - House 12
print(deliveries[-1]) # Last item - Office 8

# Adding items
deliveries.append("Apartment 3")
print(deliveries)

# Removing items
deliveries.remove("Shop 45")
print(deliveries)

# Looping through list
for address in deliveries:
    print(f"Delivering to: {address}")