import prompt


def welcome():
    prompt.PROMPT = ''
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')
    return user_name


def answer_check(user_answer, true_answer, user_name):
    if user_answer != true_answer:
        print(f'Your answer: {user_answer}')
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{true_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False
    elif user_answer == true_answer:
        print(f'Your answer: {user_answer}')
        print("Correct!")
        return True
