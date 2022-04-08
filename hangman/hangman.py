import random
from words import words
import string

# ensures that the randomly grabbed word doesn't contain a dash or space


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the use has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have used these letters: ", " ".join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print(
                    f"Letter is not in the word. Current lives is now {lives}")

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print("Invalid Character. Please Try Again")

    # gets here when length of word_letter is 0 or when lives is zero
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f'You have guessed the word: {word}')


# user_input = input("Type Something: ")
hangman()
