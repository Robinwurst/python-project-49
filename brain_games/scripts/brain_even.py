#!/usr/bin/env python3
import prompt
import random


def welcome():
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')


def even_odd():
    hidden_number = random.randint(0, 1000)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {hidden_number}')
    answer = prompt.string(prompt=None, empty=False)
    print(f'Your answer: {answer}')
    if hidden_number % 2 == 0 and answer == 'yes':
        print('Correct!')
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
