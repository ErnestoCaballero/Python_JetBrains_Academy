import random
import string

print("H A N G M A N")

def hangman_play():
    # Setting up the initial parameters of the game:
    languages = ['python'] # , 'java', 'kotlin', 'javascript']  # List of words to be choose
    choice = random.choice(languages)  # Pick a random word from the list.
    set_choice = set(choice)  # Set with the letters of the word randomly picked.
    list_choice = list(choice)  # List with the letters of the picked word
    mutable_choice = list('-' * len(choice))
    guesses = set()
    correct_guesses = set()
    lives = 8

    while True:
        print()
        print(''.join(mutable_choice))
        guess_char = input('Input a letter: ')
        if len(guess_char) > 1:
            print('You should input a single letter')
            continue
        if guess_char not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter')
            continue
        if guess_char in guesses:
            print("You already typed this letter")
        elif guess_char in set_choice:
            for i in range(len(list_choice)):
                if list_choice[i] == guess_char:
                    mutable_choice[i] = list_choice[i]
            correct_guesses.add(guess_char)
            guesses.add(guess_char)
        else:
            print('No such letter in the word')
            guesses.add(guess_char)
            lives -= 1
        if lives < 1:
            print("You are hanged!\n")
            break
        if correct_guesses == set_choice:
            print()
            print(''.join(mutable_choice))
            print('You guessed the word!\nYou survived!\n')
            break


def main():
    while True:
        initializer = input('Type "play" to play the game, "exit" to quit: ')
        if initializer == 'play':
            hangman_play()
        else:
            break

main()
