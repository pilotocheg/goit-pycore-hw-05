import re
from typing import Generator, Callable

type NumbersGenerator = Generator[float, None, None]


def generator_numbers(text: str) -> NumbersGenerator:
    for part in text.split(" "):
        # if the part is a real number - yield it
        if re.search(r"^[+-]?\d+(?:.\d+)?$", part):
            yield float(part)


def sum_profit(text: str, find_income: Callable[[str], NumbersGenerator]) -> float:
    """
    Returns the sum of all incomes in the given string found by the find_income generator func

    :param str text: text which may contain incomes (real numbers)
    :param function find_income: function which returns generator with incomes
    """

    return sum([income for income in find_income(text)], start=0.0)
