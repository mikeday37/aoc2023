from common import *
from .solve import *
from .example import _example, _example2

test(solve_part, 142, _example)
test(solve_part, 281, _example2, True)

verify_known_answer(solve_part, 55172, read_input())
verify_known_answer(solve_part, 54925, read_input(), True)