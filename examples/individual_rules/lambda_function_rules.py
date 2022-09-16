"""
----------------------------------------------------------------------------------
[2.10 Lambda Function Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#210-lambda-function-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rules `lambdas-should-be-short`, `map-lambda-to-generator` and
`filter-lambda-to-generator`.
Also note that the rules `map-lambda-to-generator` and
`filter-lambda-to-generator` have replacements, and hence Sourcery can
automatically fix them.
"""

from typing import Callable, Iterator


# no violation: small lambdas are OK
def squarer() -> Callable[[int], int]:
    """Generate a function that calculates the square of integers."""
    return lambda x: x**2


def power() -> Callable[[int], int]:
    """Generate a function that takes two `x` and `y` and calculates `x**y`."""
    return lambda x, y: x**y


# violate `lambdas-should-be-short` because those lambdas are huge!
def get_very_long_and_involved_calculator_for_x() -> Callable[[int], int]:
    """Generate a function that does a very involved calculation with `x`."""
    return lambda x: do_something_very_long_and_involved_with(x) - do_other_very_long_and_involved_things_with(x)


def get_very_long_and_involved_calculator_for_xyz() -> Callable[[int, int, int], int]:
    """Generate a function that does an involved calculation with multiple inputs."""
    return lambda x, y, z: do_something_very_long_and_involved_with(x) - do_other_very_long_and_involved_things_with(y, z)


# trigger `map-lambda-to-generator`: mapping lambdas can be refactored as Pythonic
# generators
def transform_numbers_with_lambda(numbers: list[float]) -> Iterator[float]:
    """Perform transformation in list of numbers."""

    # should be `return (x**2 for x in numbers)`
    return map(lambda x: x**2, numbers)


def transform_numbers_with_lambda_list(numbers: list[float]) -> list[float]:
    """Perform transformation in list of numbers, returning another list."""

    # should be `return [x**2 for x in numbers]`
    return list(map(lambda x: x**2, numbers))


# no violation: mapping with an existing function is alright
def transform_numbers_with_function(numbers: list[float]) -> Iterator[float]:
    """Perform transformation in list of numbers."""
    return map(squarer, numbers)


# no violation: mapping with multiple arguments is OK since the generator version would
# involve a call to `zip`, which is not necessarily cleaner
def add_numbers(left: list[float], right: list[float]) -> Iterator[float]:
    """Perform transformation in list of numbers."""
    return map(lambda x, y: x + y, left, right)


# trigger `filter-lambda-to-generator`: filtering with lambdas can be refactored as
# Pythonic generators
def filter_numbers_with_lambda(numbers: list[float]) -> Iterator[float]:
    """Filter numbers in list."""

    # should be `return (x for x in numbers if x % 2 == 0)`
    return filter(lambda x: x % 2 == 0, numbers)


def filter_numbers_with_lambda_list(numbers: list[float]) -> list[float]:
    """Filter numbers in list, returning another list"""

    # should be `return [x for x in numbers if x % 2 == 0]`
    return list(filter(lambda x: x % 2 == 0, numbers))


# no violation: mapping with an existing function is alright
def filter_numbers_with_function(numbers: list[float]) -> Iterator[float]:
    """Perform transformation in list of numbers."""
    return filter(is_even, numbers)
