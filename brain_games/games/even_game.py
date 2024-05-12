import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return "yes" if number % 2 == 0 else "no"


def gen_raund_data():
    hidden_number = random.randint(0, 1000)
    task = hidden_number
    true_answer = is_even(hidden_number)
    return true_answer, task
