import random

import sys


def guessing(guess):
    global answer
    try:
        if initial_num <= guess <= final_num:
            check_answer(guess, answer)
        else:
            print('The number is out of range')
            guessing(int(input(message)))
    except ValueError:
        print('Input an integer number within the values')
        guessing(int(input(message)))


def check_answer(num, answer):
    global counter
    total_num = (len(range(initial_num, final_num)))
    if num == answer:
        if counter <= (total_num/4):
            print('Great job! You are amazing!')
        elif counter <= (total_num/2):
            print('Good job! You did it!')
        else:
            print('Not bad! You got the number!')
        return True
    else:
        counter += 1
        print('Try again!')
        if __name__ == '__main__':
            guessing(int(input(message)))
        return False


print('''
This game consists on try to guess a random number from 1 to 10

If running through the shell terminal, you can use the command python3 randomgame.py X Y to start

In that case the random number will be any number from X  to Y

Good luck
''')
if __name__ == '__main__':

    try:
        initial_num = int(sys.argv[1])
        final_num = int(sys.argv[2])
        answer = random.randint(initial_num, final_num)
    except:
        initial_num = 1
        final_num = 10
        answer = random.randint(initial_num, final_num)

    counter = 0

    message = f'Try to guess a number from {initial_num} to {final_num}: '

    guessing(int(input(message)))
