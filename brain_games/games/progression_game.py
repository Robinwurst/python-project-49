
import random

question = "What number is missing in the progression?"


# noinspection PyTypeChecker
def start_game_progression():
    base_list_of_numbers = list(range(0, 150, random.randint(1, 10)))
    random_len = random.randint(6, 11)
    cut_list = base_list_of_numbers[:random_len]
    hidden_number = random.randint(0, random_len - 1)
    true_answer = cut_list[hidden_number]
    cut_list[hidden_number] = '..'
    refactored_list = ' '.join([str(elem) for elem in cut_list])
    task = f"{refactored_list}"
    return true_answer, task


def game_func():
    true_answer, task = start_game_progression()
    return true_answer, task
