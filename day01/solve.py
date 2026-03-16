from common import *

def solve_part(input, use_words = False):
    digits = tuple(map(str, range(1, 10)))
    checkfor = digits
    if use_words:
        names = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        digit_map = {x[0]: x[1] for x in zip(names, digits)}
        checkfor += names
    total = 0
    for line in input.splitlines():
        firsts = filter(lambda x: x[1] > -1, ((x, line.find(x)) for x in checkfor))
        lasts = filter(lambda x: x[1] > -1, ((x, line.rfind(x)) for x in checkfor))
        first = min(firsts, key = lambda x: x[1])
        last = max(lasts, key = lambda x: x[1])
        left, right = map(lambda x: x[0] if x[0].isdigit() else digit_map[x[0]], [first, last])
        total += int(left + right)
    return total

print("Part 1:", solve_part(read_input()))
print("Part 2:", solve_part(read_input(), True))

