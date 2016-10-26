import random

while (1 == 1):
    a = raw_input('Want to Play?')
    if (a == 'y'):
        r = random.randint(1, 100)
        print('Guess the Number:')
        print('The number is between 1 and 100')
        b = int(raw_input())
        if (b == r):
            print(r, 'You Won')
        elif (b != r):
            print(r, 'You Lose')
    elif (a == 'n'):
        break
    else:
        print('You Did Not Answered the Question')
