# Creating a customer record
customer = {
    "name": "Sonam",
    "area": "Babsa",
    "trips_today": 5,
    "rating": 4.8
}

# Accessing data
print(customer["name"])
print(customer["rating"])

# Adding new info
customer["phone"] = "975-1234567"
print(customer)

# Updating values
customer["trips_today"] = 8
print(customer)