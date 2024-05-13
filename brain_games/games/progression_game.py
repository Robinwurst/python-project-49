
import random

QUESTION = "What number is missing in the progression?"
MIN_LEN_OF_PROGRESSION = 6
MAX_LEN_OF_PROGRESSION = 11


# noinspection PyTypeChecker
def hide_number(cut_list, hidden_number):
    cut_list[hidden_number] = '..'
    refactored_list = ' '.join([str(elem) for elem in cut_list])
    return f"{refactored_list}"


def gen_raund_data():
    base_list_of_numbers = list(range(0, 150, random.randint(1, 10)))
    random_len = random.randint(MIN_LEN_OF_PROGRESSION, MAX_LEN_OF_PROGRESSION)
    cut_list = base_list_of_numbers[:random_len]
    hidden_number = random.randint(0, random_len - 1)
    true_answer = cut_list[hidden_number]
    task = hide_number(cut_list, hidden_number)
    return true_answer, task
