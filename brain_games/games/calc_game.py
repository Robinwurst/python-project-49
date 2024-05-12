import random

QUESTION = "What is the result of the expression?"


def calc_expression(rand_operation, first_number, second_number):
    if rand_operation == 1:
        task = f"{first_number} + {second_number}"
        true_answer = first_number + second_number
        return true_answer, task
    elif rand_operation == 2:
        task = f'{first_number} - {second_number}'
        true_answer = first_number - second_number
        return true_answer, task
    elif rand_operation == 3:
        task = f'{first_number} * {second_number}'
        true_answer = first_number * second_number
        return true_answer, task


def gen_raund_data():
    rand_operation = random.randint(1, 3)
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    true_answer, task = calc_expression(rand_operation,
                                        first_number, second_number)
    return true_answer, task
