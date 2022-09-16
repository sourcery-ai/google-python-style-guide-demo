"""
----------------------------------------------------------------------------------
[2.11 Conditional Expression Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#211-conditional-expression-rules)
----------------------------------------------------------------------------------
This example file contains pieces of code that either comply with or violate the
rule `no-complex-if-expressions`.
"""

# no violation: if-expression is short and easy to understand
def choose_one_or_two(condition: bool) -> int:
    """Choose `1` or `2` based on the input `condition`."""
    return 1 if condition else 2


# violate `no-complex-if-expressions`: the following functions all contain very long
# expressions inside the if-expressions
def choose_one_or_two_based_on_very_long_condition() -> int:
    """Choose `1` or `2` based on a condition that has a very long name."""
    return 1 if this_is_an_incredibly_long_condition_that_is_more_than_80_characters_long_no_joking_around else 2


def choose_very_long_value_or_two() -> int:
    """Choose between a very long value and `2` based on a condition."""
    return this_is_an_incredibly_long_value_that_is_more_than_80_characters_long_no_joking_around if cond else 2


def choose_one_or_very_long_value() -> int:
    """Choose between `1` and a very long value based on a condition."""
    return 1 if cond else this_is_an_incredibly_long_value_that_is_more_than_80_characters_long_no_joking_around


def choose_one_or_very_long_complex_expression() -> int:
    """Choose `1` or an expression that is very long and complex."""
    return 1 if cond else this_value(is_very_complex + and_ends_up_being_too_long, because_it_contains="nested and long expressions")
