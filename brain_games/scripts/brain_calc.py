import random
import prompt


def welcome():
    prompt.PROMPT = ''
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')
    return user_name


def calc():
    rand_operation = random.randint(1, 3)
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    if rand_operation == 1:
        print(f'What is the result of the expression?\nQuestion: {first_number} + {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number + second_number
        return user_answer, true_answer
    elif rand_operation == 2:
        print(f'What is the result of the expression?\nQuestion: {first_number} - {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number - second_number
        return user_answer, true_answer
    elif rand_operation == 3:
        print(f'What is the result of the expression?\nQuestion: {first_number} * {second_number} = ')
        user_answer = prompt.integer(prompt=None, empty=False)
        true_answer = first_number * second_number
        return user_answer, true_answer


def game_calc():
    user_name = welcome()
    user_answer, true_answer = calc()
    if user_answer != true_answer:
        print(f'Your answer: {user_answer}')
        print(f"{user_answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False
    elif user_answer == true_answer:
        print(f'Your answer: {user_answer}')
        print("Correct!")
        return True


def games_iter(true_answer=0):
    while true_answer < 3:
        result = game_calc()
        if result:
            true_answer += 1
            print(f'Your score = {true_answer}')
        else:
            print("Try again!")
            return
    print('You win!')


def main():
    games_iter()
