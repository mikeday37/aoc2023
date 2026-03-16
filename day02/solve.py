from common import *
from math import prod

def parse_pull(pull_raw):
    colors = {x[1]: int(x[0]) for x in [y.split() for y in pull_raw.split(", ")]}
    return tuple(colors[c] if c in colors else 0 for c in ("red", "green", "blue"))

def parse_game(line):
    game_part, pulls_part = line.split(': ')
    id = int(game_part.split()[1])
    pulls = map(parse_pull, pulls_part.split('; '))
    return id, pulls
    
def solve_part_1(input):
    cubes = (12, 13, 14)
    def is_possible(pull):
        return all(c[0] <= c[1] for c in zip(pull, cubes))
    return sum(id for id, pulls in map(parse_game, input.splitlines()) 
               if all(is_possible(pull) for pull in pulls))

def solve_part_2(input):
    return sum(prod(max(c) for c in zip(*pulls))
               for _, pulls in map(parse_game, input.splitlines()))

print("Part 1:", solve_part_1(read_input()))
print("Part 2:", solve_part_2(read_input()))
