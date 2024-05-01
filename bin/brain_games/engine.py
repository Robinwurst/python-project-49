from bin.brain_games.modules.game_modules import answer_check, welcome


def engine(game_func, question):
    """Движок для игр. Принимает аргументы:
    true_answer, user_answer, question"""
    welcome()
    score = 0
    while score < 3:
        user_answer, true_answer = game_func(question)
        if answer_check(user_answer, true_answer):
            score += 1
            print(f'Your score {score} from 3')
        else:
            return
    print("You win!")
