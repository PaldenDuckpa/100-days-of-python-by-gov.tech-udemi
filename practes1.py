print("welcome to tip calculator")
bill = float(input("what was the total bill? Nu "))
tip = int(input("what percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
total_tip = bill * (tip / 100)
print(f"total tip is {total_tip}")
print(f"total bill is {bill + total_tip}")
total_bill = bill + total_tip
if people > 0:
	per_person = total_bill / people 
	print(f"Each person should pay: {per_person}")
else:
	print("Number of people must be greater than zero.")
