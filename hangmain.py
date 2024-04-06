import random
import hangman_art
import hangman_wordlist

print(hangman_art.logo)

game_end = False

chosen_word = random.choice(hangman_wordlist.word_list)

lives = 6
display = []
for _ in range(len(chosen_word)):
    display += "_"

while not game_end:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_end = True
            print("You lose")

    print(' '.join(display))

    if "_" not in display:
        game_end = True
        print("You win!")

    print(hangman_art.stages[lives])






