import random


def play():
    choices = ['r', 's', 'p']
    user = input(
        "What is your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors :")
    computer = random.choice(choices)

    if user == computer:
        return f'It\'s a tie, You chose {user} and the computer chose {computer}'

    if is_win(user, computer):
        return f'You won! You chose {user} and the computer chose {computer}'

    return 'You lost!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
