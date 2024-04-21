from brain_games.engine import engine
from brain_games.games.calc_game import *


def main(game_name=None):
    engine(game_name)


if __name__ == '__main__':
    main(calc())