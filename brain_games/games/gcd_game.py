import math
import random
import prompt

question = "Find the greatest common divisor of given numbers.\nQuestion:"


def start_game_gcd(question):
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    true_answer = math.gcd(first_number, second_number)
    print(f"{question} {first_number} {second_number}")
    user_answer = prompt.integer(prompt=None, empty=False)
    return user_answer, true_answer


def game_func(question):
    user_answer, true_answer = start_game_gcd(question)
    return user_answer, true_answer
