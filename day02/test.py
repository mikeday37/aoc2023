from common import *
from .solve import *
from .example import _example

test(solve_part_1, 8, _example)
test(solve_part_2, 2286, _example)

verify_known_answer(solve_part_1, 2164, read_input())
verify_known_answer(solve_part_2, 69929, read_input())
