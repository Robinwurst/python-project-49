import prompt



def welcome():
    prompt.PROMPT = ''
    print("Welcome to the Brain Games!\nMay I have your name?")
    user_name = prompt.string(prompt=None, empty=False)
    print(f'Hello, {user_name}!')
    return user_name


# def score_check(result_of_check_answer, true_answer=0):
#     while true_answer < 3:
#         result = result_of_check_answer
#         if result:
#             true_answer += 1
#             print(f'Your score = {true_answer}')
#         else:
#             print("Try again!")
#             return
#     print(f'Congratulations, {user_name}!')


def answer_check(user_answer, true_answer, user_name):
    if user_answer != true_answer:
        print(f'Your answer: {user_answer}')
        print(f"{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{true_answer}'.")
        print(f"Let's try again, {user_name}!")
        return False
    elif user_answer == true_answer:
        print(f'Your answer: {user_answer}')
        print("Correct!")
        return True
