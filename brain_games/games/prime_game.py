import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_primes(n):
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return primes


def is_prime(primes_list, question_number):
    if question_number in primes_list:
        true_answer = 'yes'
        return true_answer
    else:
        true_answer = 'no'
        return true_answer


def start_game_prime():
    question_number = random.randint(1, 200)
    primes_list = get_primes(200)
    true_answer = is_prime(primes_list, question_number)
    task = f"{question_number}"
    return true_answer, task


def game_func():
    true_answer, task = start_game_prime()
    return true_answer, task
