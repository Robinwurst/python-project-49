import random
import numpy
import prompt

question = ('Answer "yes" if given number is prime. Otherwise answer "no".'
            '\nQuestion: ')


def get_primes(n):
    sieve = numpy.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return numpy.r_[2, 2 * numpy.nonzero(sieve)[0][1::] + 1]


def is_prime(primes_list, question_number):
    if question_number in primes_list:
        true_answer = 'yes'
        return true_answer
    else:
        true_answer = 'no'
        return true_answer


def start_game_prime(question):
    question_number = random.randint(1, 200)
    primes_list = get_primes(200)
    true_answer = is_prime(primes_list, question_number)
    print(f"{question}{question_number}")
    user_answer = prompt.string(prompt=None, empty=False)
    return user_answer, true_answer


def game_func(question):
    user_answer, true_answer = start_game_prime(question)
    return user_answer, true_answer
