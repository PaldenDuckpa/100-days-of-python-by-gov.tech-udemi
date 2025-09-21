"""  creat a taxi app
used a,if , elif ,else
       b,creat place and taxi fee data base 
       c, used input function and all  """


bill = 0
print("welcome to my taxi app service")
location = input("where do you want me to pick you up?")
dastination = input("where do you want to go?")

# database of locations and their respective costs
place = {'toun to olakha': 'NU 120', 'toun to babsa': 'NU 150', 'toun to dechen': 'NU 200', 'toun to depse': 'NU 250', 'toun to kabsa': 'NU 300'}

location = "toun"
destination = "olakha"
print(f"you are going from {location} to {destination}")

# cost calculation based on destination
if dastination == "olakha":
    bill = 120
elif dastination == "babsa":
    bill = 150
elif dastination == "dechen":
    bill = 200
elif dastination == "depse":
    bill = 250
elif dastination == "kabsa":
    bill = 300
else:
    print("Sorry, destination not found.")
    bill = 0
print(f"Your bill is NU {bill}")
if dastination == "olakha":
    bill = 120,

elif dastination == "babsa":
    bill = 150
    




