# DELIVERY DECISION MAKER – Your smart assistant!

print("===== DELIVERY DECISION MAKER 3000 =====")

# Get input from you
distance = float(input("How many kilometers to the customer? "))
traffic = input("Traffic level (low/medium/heavy): ").lower()
weather = input("Weather (sunny/rainy/stormy): ").lower()
package_weight = float(input("Package weight in kg: "))

# Let Python make decisions!

# Decision 1: Can you carry it?
if package_weight > 30:
    print("\n WARNING: Package is too heavy! Need help!")
elif package_weight > 20:
    print("\n Heavy package – be careful with your back!")
else:
    print("\n Package weight is fine!")

# Decision 2: Which route to take?
if traffic == "heavy" and weather == "stormy":
    print(" BAD combo! Suggest waiting 15 minutes.")
elif traffic == "heavy" and distance > 10:
    print(" Take the highway – it's longer but faster now.")
elif traffic == "low":
    print(" Take the shortest route – you'll be fast!")
else:
    print(" Take your normal route.")

# Decision 3: Estimated time
if distance <= 3:
    time = 10
elif distance <= 7:
    time = 20
elif distance <= 15:
    time = 35
else:
    time = 50

# Adjust for weather
if weather == "rainy":
    time = time + 10
elif weather == "stormy":
    time = time + 20

print(f"\n Estimated delivery time: {time} minutes")

# Decision 4: Should you call the customer?
if weather == "stormy" or distance > 15:
    print(" Call customer to inform about possible delay.")
else:
    print(" No call needed – you're on track!")

print("\n===== DRIVE SAFE! =====")