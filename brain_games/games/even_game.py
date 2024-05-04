import random

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_game_even_odd():
    hidden_number = random.randint(0, 1000)
    task = hidden_number
    if hidden_number % 2 == 0:
        true_answer = "yes"
        return true_answer, task
    elif hidden_number % 2 != 0:
        true_answer = "no"
        return true_answer, task


def game_func():
    true_answer, task = start_game_even_odd()
    return true_answer, task
