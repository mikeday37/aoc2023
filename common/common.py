import sys
from pathlib import Path
import inspect
import os

def read_input():
    input_path = Path(sys.argv[0]).parent / "input.txt"
    assert os.path.exists(input_path), "input.txt must exist in the same dir as the script being run"
    with open(input_path) as file:
        content = file.read()
    return content

_test_counter = 0

def test(function, expected_return_value, *args):
    global _test_counter
    _test_counter += 1

    calling_frame = inspect.currentframe().f_back
    calling_filename = calling_frame.f_code.co_filename
    calling_linenumber = calling_frame.f_lineno

    actual_return_value = function(*args)

    if actual_return_value == expected_return_value:
        status = "PASS"
        suffix = ""
    else:
        status = f" !! FAIL !!  (expected={expected_return_value}, actual={actual_return_value})"
        suffix = f" at file \"{calling_filename}\", line {calling_linenumber}"

    print(f"TEST #{_test_counter}, {function.__name__}: {status}{suffix}")

def verify_known_answer(function, known_answer, *args):
    """
    This function will do nothing unless the cwd of the process contains the file:
        .enable_verify_known_answer

    The known answers in my test cases are only valid for my input files.  The creator
    of Advent of Code does not want people publishing puzzle inputs, and I respect that.
    """
    if os.path.exists(".enable_verify_known_answer"):
        test(function, known_answer, *args)