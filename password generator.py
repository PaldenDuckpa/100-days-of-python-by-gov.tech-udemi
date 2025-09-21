# creat password generator
# it should give password of length 0f 8 to 12 characters
# must have following characters:
# 1, it must give different password each time 
# 2, it must be in different lengths 
# 3, it must have at least one upercase later 
# 

import random

letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = letters.upper()
digits = "012345689"
charactors = "!@#$%^&*()_=+{}[]:;\"'<>,.?/"

# method one 

'''print("welcome to python password generator")
def generate_password():
    length = random.randint(8, 12)
    password = []

    # Ensure at least one uppercase letter
    password.append(random.choice(uppercase_letters))
    
    # Ensure at least one digit
    password.append(random.choice(digits))
    
    # Ensure at least one special character
    password.append(random.choice(charactors))

    # Fill the rest of the password length with random choices from all characters
    all_characters = letters + uppercase_letters + digits + charactors
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)'''


# method two 
print("Welcome to Python Password Generator")
nr_letters = int(input("how maney letters would you like in your password?\n"))
nr_uppercase = int(input("how maney uppercase letters would you like?\n"))
nr_digits = int(input("how maney numbers would you like?\n"))
nr_charactors = int(input("how maney charactors would you like?\n"))


password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_uppercase + 1):
    password_list.append(random.choice(uppercase_letters))

for char in range(1, nr_digits + 1):
    password_list.append(random.choice(digits))

for char in range(1, nr_charactors + 1):
    password_list.append(random.choice(charactors)) 

random.shuffle(password_list)
print(password_list)




