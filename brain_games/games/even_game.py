import random
import prompt

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_odd(question):
    prompt.PROMPT = ''
    hidden_number = random.randint(0, 1000)
    print(question)
    print(f'Question: {hidden_number}')
    user_answer = prompt.string(prompt=None, empty=False)
    if hidden_number % 2 == 0:
        return user_answer, "yes"
    elif hidden_number % 2 != 0:
        return user_answer, "no"


def game_func(question):
    user_answer, true_answer = even_odd(question)
    return user_answer, true_answer
