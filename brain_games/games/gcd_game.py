import math
import random

QUESTION = "Find the greatest common divisor of given numbers."
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 30

def search_gcd(first_number, second_number):
    true_answer = math.gcd(first_number, second_number)
    return true_answer


def gen_raund_data():
    first_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    second_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    task = f"{first_number} {second_number}"
    true_answer = search_gcd(first_number, second_number)
    return true_answer, task
