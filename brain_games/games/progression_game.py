
import random
import prompt

question = "What number is missing in the progression?\nQuestion: "


def start_game_gcd(question):
    base_list_of_numbers = list(range(0, 150, random.randint(1, 10)))
    cut_list = base_list_of_numbers[:11]
    hidden_number = random.randint(0, 11)
    true_answer = cut_list[hidden_number]
    cut_list[hidden_number] = '..'
    print(f"{question}{cut_list}")
    user_answer = prompt.integer(prompt=None, empty=False)
    return user_answer, true_answer


def game_func(question):
    user_answer, true_answer = start_game_gcd(question)
    return user_answer, true_answer
