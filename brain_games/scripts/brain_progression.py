#!/usr/bin/env python3
from brain_games.engine import engine
from brain_games.games.progression_game import (gen_raund_data,
                                                QUESTION)


def main():
    engine(gen_raund_data, QUESTION)


if __name__ == '__main__':
    main()
