#!/usr/bin/env python3
import prompt
import random


def welcome():
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')


def even_odd():
    prompt.PROMPT = 'Your answer? '
    hidden_number = random.randint(0, 1000)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {hidden_number}')
    answer = prompt.string(prompt=None, empty=False)
    print(f'Your answer: {answer}')
    if hidden_number % 2 == 0 and answer == 'yes':
        print('Correct!')
        return True
    elif hidden_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False


def games_iter(true_answer=0):
    result = even_odd()
    while true_answer < 2:
        if not result:
            print("Try again!")
            games_iter(0)
        elif result:
            true_answer += 1
            print(f'{"Your score = " + str(true_answer)}')
            games_iter(true_answer)
        print('You win!')
        return


games_iter()
