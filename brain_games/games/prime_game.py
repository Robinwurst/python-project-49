import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LIMIT_NUMBERS = 200
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 200

def is_prime(number, limit_of_numbers):
    sieve = [True] * limit_of_numbers
    primes = []
    for p in range(2, limit_of_numbers):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit_of_numbers, p):
                sieve[i] = False
    return number in primes


def gen_raund_data():
    random_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    true_answer = "yes" if is_prime(random_number, LIMIT_NUMBERS) else "no"
    task = f"{random_number}"
    return true_answer, task
