import random

def NumberGuessing(num):
    compChoice = random.randint(1,9)
    
    if compChoice == num:
        print('You guessed the number')
    else:
        print('You didn\'t guess the number')

num = int(input('Can you guess the number?'))
NumberGuessing(num)