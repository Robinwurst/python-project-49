from brain_games.games.calc_game import calc
from modules.game_modules import *


def engine():
    welcome()
    while answer_check(calc()):
        score_check(answer_check(calc()))
    else:
        return


engine()
