import random

QUESTION = "What is the result of the expression?"
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 30


def calculate(rand_operation, first_number, second_number):
    if rand_operation == "+":
        return first_number + second_number
    elif rand_operation == "-":
        return first_number - second_number
    elif rand_operation == "*":
        return first_number * second_number


def gen_raund_data():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operators = ("-", "+", "*")
    rand_operation = random.choice(operators)
    task = f'{first_number} {rand_operation} {second_number}'
    true_answer = calculate(rand_operation, first_number, second_number)
    return true_answer, task
