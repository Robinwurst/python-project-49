from brain__games.modules.game_modules import answer_check, welcome


def engine(game_func):
    """Движок для игр. Принимает аргументы: true_answer, user_answer, question"""
    welcome()
    score = 0
    while score < 3:
        user_answer, true_answer, questions = game_func()
        if answer_check(user_answer, true_answer):
            score += 1
        else:
            return
    print("You win!")
