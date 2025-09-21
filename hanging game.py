import random
word_list = ["python", "java", "kotlin", "javascript ", "hangman"]
chosen_word = random.choice(word_list)
print(chosen_word)

# Randomly select a word from the list
placeholder = ""
word_lenth = len(chosen_word)
for position in range(word_lenth):
    placeholder += "-"
print(placeholder)

guess = input("Guess a letter: ").lower()
#ask the use
display = ""
#check if the letter is in the word
for letter in word_list:
    if letter in guessed_letters:
        display += letter
    else:
        display += "-"

print(display)        

        #rint("-", end=" ")