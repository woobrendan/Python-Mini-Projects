import random
import math


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    guess = random.randint(low, high)
    while feedback != 'c':
        print(f'low is {low}, high is {high}')
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)??: ").lower()
        if feedback == 'h':
            high = guess
            guess = math.ceil((high + low)/2)
        elif feedback == 'l':
            low = guess
            guess = math.ceil((high + low)/2)
        elif feedback == "c":
            break
        else:
            print("Invalid entry try again")
    print(f'Yay I knew the number was {guess}')


# guess(10)
computer_guess(100)
