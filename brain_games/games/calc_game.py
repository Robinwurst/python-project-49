import random
import prompt


def calc():
    rand_operation = random.randint(1, 3)
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    if rand_operation == 1:
        print(f'What is the result of the expression?\nQuestion: {first_number} + {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number + second_number
        return user_answer, true_answer
    elif rand_operation == 2:
        print(f'What is the result of the expression?\nQuestion: {first_number} - {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number - second_number
        return user_answer, true_answer
    elif rand_operation == 3:
        print(f'What is the result of the expression?\nQuestion: {first_number} * {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number * second_number
        return user_answer, true_answer