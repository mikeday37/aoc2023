from common import *
import itertools as it

def solve_part_1(input):
    total = 0
    for line in input.splitlines():
        digits = [ch for ch in line if ch.isdigit()]
        total += int(digits[0] + digits[-1])
    return total

def solve_part_2(input):
    digits = tuple(map(str, range(1, 10)))
    names = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    digit_map = {x[0]: x[1] for x in it.chain(zip(names, digits), zip(digits, digits))}
    total = 0
    for line in input.splitlines():
        firsts = filter(lambda x: x[1] > -1, ((x, line.find(x)) for x in digit_map))
        lasts = filter(lambda x: x[1] > -1, ((x, line.rfind(x)) for x in digit_map))
        first = min(firsts, key = lambda x: x[1])
        last = max(lasts, key = lambda x: x[1])
        left, right = map(lambda x: digit_map[x[0]], [first, last])
        total += int(left + right)
    return total

print("Part 1:", solve_part_1(read_input()))
print("Part 2:", solve_part_2(read_input()))

