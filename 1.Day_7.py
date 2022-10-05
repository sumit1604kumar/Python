#Hangman game
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["sumit", "anju", "mummy","papa","ashish","amit"]
chosen_word = random.choice(word_list)
print(f"The word selected by the computer from the list is, {chosen_word}")

# guess = input("Guess a letter: ").lower()

display = []
word_length = len(chosen_word)
end_of_game = False
lives = 6

for x in range(word_length):
    display = display + list("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game = True
            print(" You lost the game")

    # print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])
