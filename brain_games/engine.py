import prompt
prompt.PROMPT = ''
MAX_GAME_SCORE = 3


def engine(raund_data, question):
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')
    game_score = 0
    while game_score < MAX_GAME_SCORE:
        true_answer, task = raund_data()
        user_answer = input(f"{question}\nQuestion: {task}\n")
        if user_answer == str(true_answer):
            print(f'Your answer: {user_answer}')
            print("Correct!")
            game_score += 1
        else:
            print(f'Your answer: {user_answer}')
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{true_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
