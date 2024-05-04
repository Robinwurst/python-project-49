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
    """Движок для игр. Принимает аргументы:
    true_answer, user_answer, question"""
    user_name = welcome()
    score = 0
    while score < 3:
        user_answer, true_answer = game_func(question)
        if answer_check(user_answer, true_answer, user_name):
            score += 1
            # print(f'Your score {score} from 3')
        else:
            return
    print(f'Congratulations, {user_name}!')
