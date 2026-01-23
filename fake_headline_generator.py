import random

# creating subjects
subjects = [
    "tinten", "sonam choden", "penjo", "miss black", "aunte tin ton"
]

actions = ["rape", "murder", "crash", "propose"]  

places_or_things = ["mane trafick", "norling hotal", "clock toure", "club viva"]

while True:
    subject = random.choice(subjects)
    action_word = random.choice(actions)  # Changed variable name to avoid conflict
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action_word} {place_or_thing}"
    print("\n" + headline)
    user_input = input("\nDo you want another headline? (yes/no): ").strip()
    if user_input.lower() == "no":  # Added .lower() to handle "No", "NO", etc.
        break

# print goodbye message
print("thanks for using my software")
