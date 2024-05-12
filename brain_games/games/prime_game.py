import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_primes(limit_of_numbers):
    sieve = [True] * limit_of_numbers
    primes = []
    for p in range(2, limit_of_numbers):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit_of_numbers, p):
                sieve[i] = False
    return primes


def is_prime(primes_list, number):
    return "yes" if number in primes_list else "no"


def gen_raund_data():
    random_number = random.randint(1, 200)
    primes_list = get_primes(200)
    true_answer = is_prime(primes_list, random_number)
    task = f"{random_number}"
    return true_answer, task
