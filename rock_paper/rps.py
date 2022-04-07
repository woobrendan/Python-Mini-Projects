import random


def play():
    choices = ['r', 's', 'p']
    user = input(
        "What is your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    computer = random.choice(choices)

    # Check that user input is a valid rps choice
    if user not in choices:
        return "Invalid input"

    compPick = full_word(computer)
    userPick = full_word(user)

    if user == computer:
        return f'It\'s a tie, You chose {userPick} and the computer chose {compPick}'

    if is_win(user, computer):
        return f'You won! You chose {userPick} and the computer chose {compPick}'

    return f'You lost! You chose {userPick} and the computer chose {compPick}'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def full_word(letter):
    fullWords = ['Rock', 'Scissors', 'Paper']
    choices = ['r', 's', 'p']
    for index, choice in enumerate(choices):
        if choice == letter:
            return fullWords[index]


print(play())
# print(full_word('s'))
