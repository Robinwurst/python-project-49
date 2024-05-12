#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.progression_game import (gen_raund_data,
                                                QUESTION)


def main():
    run_game(gen_raund_data, QUESTION)


if __name__ == '__main__':
    main()
