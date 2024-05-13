import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 1000


def is_even(number):
    return number % 2 == 0


def gen_raund_data():
    hidden_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    task = hidden_number
    true_answer = "yes" if is_even(hidden_number) else "no"
    return true_answer, task
