#!/usr/bin/env python3
from bin.brain_games.engine import engine
from bin.brain_games.games.progression_game import game_func, question


def main():
    engine(game_func, question)


if __name__ == '__main__':
    main()
