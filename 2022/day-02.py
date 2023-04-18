import os

file_name = "{dir}/data/day-02.txt".format(dir=os.path.dirname(__file__))


def games() -> list[tuple[str, str]]:
    with open(file_name, "rt") as file:
        return [tuple(game.split(" "))
                for game
                in file.read().splitlines()]


ROCK1, PAPER1, SCISSORS1 = 'X', 'Y', 'Z'
ROCK2, PAPER2, SCISSORS2 = 'A', 'B', 'C'
LOSE, DRAW, WIN = 'X', 'Y', 'Z'

wins = {ROCK1: SCISSORS2, PAPER1: ROCK2, SCISSORS1: PAPER2}
draw = {ROCK1: ROCK2, PAPER1: PAPER2, SCISSORS1: SCISSORS2}
scores = {ROCK1: 1, PAPER1: 2, SCISSORS1: 3}

strat = {LOSE: {ROCK2: SCISSORS1, PAPER2: ROCK1, SCISSORS2: PAPER1},
         WIN:  {ROCK2: PAPER1, PAPER2: SCISSORS1, SCISSORS2: ROCK1},
         DRAW: {ROCK2: ROCK1, PAPER2: PAPER1, SCISSORS2: SCISSORS1}}


def play(game: tuple[str, str]) -> int:
    them, us = game
    if draw[us] == them:
        return scores[us] + 3
    if wins[us] == them:
        return scores[us] + 6
    return scores[us]


def sum_all_scores(games: list[tuple[str, str]]) -> int:
    return sum([play(game) for game in games])


def apply_strat(game: tuple[str, str]) -> tuple[str, str]:
    them, strategy = game
    return them, strat[strategy][them]


def play_by_the_rules(games: list[tuple[str, str]]) -> int:
    return sum([play(apply_strat(game)) for game in games])


print(sum_all_scores(games()))
print(play_by_the_rules(games()))
