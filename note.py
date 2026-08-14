#loops and repated task otomation 

#while loop (while condition "do this agen and agen ")
"""
fuel = 0
while fuel < 10:
    print(f"filling fuel... {fuel} liters done")
    fuel = fuel + 1 #incrase fuel by 1
print("tank is FULL! lets go!")
   """

#for loop (do something with each item)
"""
deliveries = ["house 12" "shot 10" "office 16" "apartment 13"]

print("starting my route!")
for address in deliveries:
    print(f"delivering package to : {address}")
print("all deliveries done!")    
"""

#The MAGIC range() Function
"""
you saw range(num_deliveries) up there. It's super useful!

    range(5) = [0, 1, 2, 3, 4] (Starts at 0 by default!)

    range(1, 6) = [1, 2, 3, 4, 5] (Starts at 1, ends before 6)


    for number in range(1, 11):
    print(f"Delivery #{number}")

    """


# DAY 3: DAILY ROUTE PLANNER

print("=====  DELIVERY ROUTE PLANNER =====\n")

# 1. WHILE LOOP: Counting trips based on fuel
total_fuel = int(input("How many liters of fuel do you have? "))
fuel_used_per_trip = 2
trips_possible = 0

print("\n--- Fuel Check ---")
while total_fuel >= fuel_used_per_trip:
    total_fuel = total_fuel - fuel_used_per_trip
    trips_possible = trips_possible + 1
    print(f" Trip {trips_possible} done. Fuel left: {total_fuel}L")

print(f"You can do {trips_possible} trips with this fuel!\n")

# 2. FOR LOOP: Entering delivery addresses
num_deliveries = int(input("How many deliveries do you have today? "))

# Create an empty list to store addresses
addresses = []

# This loop runs 'num_deliveries' times
for i in range(num_deliveries):
    address = input(f"Enter address for delivery #{i+1}: ")
    addresses.append(address)  # Add to our list

# 3. FOR LOOP: Display your entire route
print("\n---  YOUR ROUTE FOR TODAY ---")
count = 1
for location in addresses:
    print(f"Stop {count}: {location}")
    count = count + 1

print("\n Route locked! Drive safe and earn that money!")
