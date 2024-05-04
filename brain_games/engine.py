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


def engine(game_func, question):
    second_question = "\nQuestion:"
    user_name = welcome()
    score = 0
    while score < 3:
        true_answer, task = game_func()
        user_answer = input(f"{question}{second_question} {task}\n")
        if answer_check(user_answer, str(true_answer), user_name):
            score += 1
        else:
            return
    print(f'Congratulations, {user_name}!')
