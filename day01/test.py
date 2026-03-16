from common import *
from .solve import *
from .example import _example, _example2

test(solve_part_1, 142, _example)
test(solve_part_2, 281, _example2)

verify_known_answer(solve_part_1, 55172, read_input())
verify_known_answer(solve_part_2, 54925, read_input())