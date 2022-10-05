from typing import Callable

from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.recursion import get_factorial
from sort.fusion import sort as fusion_sort

tests: list[dict] = [
  {
    "input": [1, 2, 3, 4, 5],
    "expected": [1, 2, 3, 4, 5]
  },
  {
    "input": [73, 16, 829, 2, 6],
    "expected": [2, 6, 16, 73, 829]
  },
  {
    "input": [-4, -282, 0, 7, 0],
    "expected": [-283, -4, 0, 0, 7]
  },
  {
    "input": [1, 1, 1, 1, 1],
    "expected": [1, 1, 1, 1, 1]
  },
  {
    "input": [],
    "expected": []
  },
  {
    "input": [8],
    "expected": [8]
  }
]


def test_sort_function(sort_function: Callable, label: str):
    error = False

    for test in tests:
        result = sort_function(test["input"])

        if len(result) != len(test["input"]):
            error = True
            break

        for index, number in enumerate(result):
            if number != test["input"][index]:
                error = True
                break

    print(label, '\033[91m❌KO\033[00m' if error else '\033[92m✓ OK\033[00m')


def test_factorial():
    correct: bool = (
        get_factorial(1) == 1
        and get_factorial(2) == 2
        and get_factorial(5) == 120
        and get_factorial(10) == 3628800
    )

    print(
      "Factorielle",
      '\033[92m✓ OK\033[00m' if correct else '\033[91m❌KO\033[00m'
    )


test_sort_function(insertion_sort, "Test par insertion")
test_sort_function(selection_sort, "Test par sélection")
test_factorial()
test_sort_function(selection_sort, "Test par fusion")
