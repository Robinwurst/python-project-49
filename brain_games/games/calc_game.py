import random

question = "What is the result of the expression?"


# user_answer = prompt.integer(prompt=None, empty=False)

def start_game_calc():
    rand_operation = random.randint(1, 3)
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
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


def game_func():
    true_answer, task = start_game_calc()
    return true_answer, task
