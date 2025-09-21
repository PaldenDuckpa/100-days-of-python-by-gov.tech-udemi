# rock paper scissers game



import random

print(" Welcome to Rock Paper Scissors Game! ")
print("=" * 40)

while True:
    print("\nChoose your move:")
    print("1. Rock ")
    print("2. Paper ")
    print("3. Scissors ")
    print("4. Quit ")
    
    # Get user choice
    user_input = input("\nEnter your choice (1-4): ")
    
    # ash if u want to play continue 
    if user_input == "4":
        print("Thanks for playing! Goodbye! ")
        break
    
    # Validate user input
    if user_input not in ["1", "2", "3"]:
        print(" Invalid choice! Please enter 1, 2, or 3.")
        continue
    
    user_choice = int(user_input)
    
    # Computer makes random choice
    computer_choice = random.randint(1, 3)
    
    
    choices = {
        1: "Rock ",
        2: "Paper ", 
        3: "Scissors "
    }
    
    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    print("-" * 30)
    
    # Determine winner 
    if user_choice == computer_choice:
        print(" It's a tie! Play again!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print(" You win! Congratulations!")
    else:
        print(" Computer wins! Better luck next time!")
    
    print("=" * 40)
