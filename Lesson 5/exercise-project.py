##Make a program that randomly guesses numbers.##
from random import *

print('Guess the number! It\'s between 1 and 100')

num = randint(1, 100)

def guess():
    try:
        global numGuess
        numGuess = int(input())
        numFunc(numGuess)
    except ValueError:
        print('Please enter a number!')
        guess()

def numFunc(numGuess):
    if numGuess < num:
        print('Try higher!')
        guess()
    elif numGuess > num:
        print('Try lower!')
        guess()
    elif numGuess == num:
        print('Correct number! You win!')

guess()