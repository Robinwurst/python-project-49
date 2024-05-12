import math
import random

QUESTION = "Find the greatest common divisor of given numbers."


def search_gcd(first_number, second_number):
    true_answer = math.gcd(first_number, second_number)
    return true_answer


def gen_raund_data():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    task = f"{first_number} {second_number}"
    true_answer = search_gcd(first_number, second_number)
    return true_answer, task
