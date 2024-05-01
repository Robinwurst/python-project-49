#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.gcd_game import game_func, question


def main():
    engine(game_func, question)


if __name__ == '__main__':
    main()
