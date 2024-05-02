
import random
import prompt

question = "What number is missing in the progression?\nQuestion:"


# noinspection PyTypeChecker
def start_game_gcd(question):
    base_list_of_numbers = list(range(0, 150, random.randint(1, 10)))
    random_len = random.randint(6, 11)
    cut_list = base_list_of_numbers[:random_len]
    hidden_number = random.randint(0, random_len)
    true_answer = cut_list[hidden_number]
    cut_list[hidden_number] = '..'
    refactored_list = ' '.join([str(elem) for elem in cut_list])
    print(f"{question} {refactored_list}")
    user_answer = prompt.integer(prompt=None, empty=False)
    return user_answer, true_answer


def game_func(question):
    user_answer, true_answer = start_game_gcd(question)
    return user_answer, true_answer
