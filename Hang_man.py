import random

# 🎮 Welcome screen
print("""
**********************************
   Welcome to "Hangman Game!"
**********************************

Description:
Hangman is a fun guessing game where a secret word 
is chosen randomly. Your goal is to guess the word one 
letter at a time. 

Be careful! Each wrong guess brings the hangman closer 
to his fate. You only have 6 tries...

Good luck! 
""")

# Word bank by difficulty
easy_words = [
    "dog", "cat", "sun", "car", "hat", "pen", "box", "fish", "tree", "milk"
]
medium_words = [
    "planet", "family", "school", "orange", "castle", "window",
    "guitar", "bridge", "garden", "rabbit"
]
hard_words = [
    "computer", "elephant", "hangman", "language", "university",
    "astronomy", "keyboard", "mountain", "airplane", "strategy"
]

# Difficulty choice
difficulty = ""
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()

if difficulty == "easy":
    words = easy_words
elif difficulty == "medium":
    words = medium_words
else:
    words = hard_words

# Hangman stages
hangman_stages = [
'''
 +---+
     |
     |
     |
     |
     |
======== ''',
'''
 +---+
 |   |
     |
     |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
     |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
======== ''',
'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
======== ''',
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
''']

# Pick random word
random_word = random.choice(words)

# Setup game
display = ["_"] * len(random_word)
print("\n" + " ".join(display))
lives = 6
guessed_letters = []
print(hangman_stages[0])

# Game loop
while "_" in display and lives > 0:
    guess = input("Please guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that. Try again.")
        print(f"You have {lives} tries left")
        continue
    guessed_letters.append(guess)
    if guess not in random_word:
        lives -= 1
        print(hangman_stages[6 - lives])
    else:
        for position in range(len(random_word)):
            if random_word[position] == guess:
                display[position] = guess
    print(' '.join(display))
    print(f"You have {lives} tries left\n")
    print()
    
# End game
if lives == 0:
    print("You lose!")
    print(f"The word was: {random_word}")
    print(hangman_stages[-1])
else:
    print("""
************
YOU WIN!
************
""")
