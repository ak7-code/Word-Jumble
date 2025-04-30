import random 
import os
os.system('cls')

# Code adapted from GeeksforGeeks, 
# https://www.geeksforgeeks.org/python-os-path-abspath-method-with-example/, 
# https://www.geeksforgeeks.org/python-os-path-dirname-method/,
# https://www.geeksforgeeks.org/python-os-path-join-method/,
# 25/04/2025 1:55PM
current_dir = os.path.dirname(os.path.abspath(__file__)) # Locates current directory of this file
file_path = os.path.join(current_dir, 'words.txt') # Joins words.txt to the current directory

# CHATGPT, "Generate me 70 software-engineering related words. No acronyms. Print the list with commas. 
# Put "" on each word. No capital letters.", 16/04/2025 4:30PM
# Code adapted from GeeksforGeeks, https://www.geeksforgeeks.org/with-statement-in-python/,
# 23/04/2025 2:23PM
with open(file_path, "r") as f:
    list = [line.strip() for line in f] # Converts words.txt to a list

word = random.choice(list)
correct = word
jumble = ""

# Code adapted from OneCompiler, https://onecompiler.com/python/3x4yq2vgb, 16/04/2025 at 4:02PM
# Word Jumbler
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

turns = 1
x = 7 # Predefined number of attempts player has (minus one)
win = False
print(f"\nThe jumble is: {jumble}")

while turns < x and win == False: 
  while turns < 4: # Before the player gets their hint
    for char in correct:
      print("_", end="") # Prints the underscores (horizontally)
    print("\n")
    guess = input("Guess the word: ").lower() 
    if len(guess) != len(correct): # Ensuring they are legitimate guesses
      print("Not the same amount of characters!")
    elif guess == correct:
      win = True # Important for determining the displayed end message
      break
    else:
      print(f"Wrong. You have {x - turns - 1} guesses left.")
      turns += 1
  if turns < x and win == False: 
    print("\n")
    print(f"The first letter is: {correct[:1]}") # [:1] used to determine the first letter
  while turns >= 4 and turns < x:
    print (correct[:1], end=""),
    for char in correct[1:]:
      print ("_", end="")
    print ("\n")
    guess = input("Guess the word: ").lower()
    if len(guess) != len(correct):
      print("Not the same amount of characters!")
    elif guess == correct:
      win = True 
      break
    else:
      print(f"Wrong. You have {x - turns - 1} guesses left.")
      turns += 1
      

if win == True: # Determining whether or not to display the 'win' message.
  print(f"Good job! You won in {turns} attempt/s.")
else: 
  print(f"You lost. The word was \'{correct}\'.")