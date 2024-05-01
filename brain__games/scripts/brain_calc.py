from brain__games.engine import engine
from brain__games.games.calc_game import game_func, question


def main():
    engine(game_func, question)


if __name__ == '__main__':
    main()
