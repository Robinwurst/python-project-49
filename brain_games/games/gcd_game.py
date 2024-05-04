import math
import random

question = "Find the greatest common divisor of given numbers."


def start_game_gcd():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    true_answer = math.gcd(first_number, second_number)
    task = f"{first_number} {second_number}"
    return true_answer, task


def game_func():
    true_answer, task = start_game_gcd()
    return true_answer, task
