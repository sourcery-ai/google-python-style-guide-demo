"""
----------------------------------------------------------------------------------
[2.21 Type Annotation Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#221-type-annotation-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rules `require-parameter-annotation` and `require-return-annotation`.
"""

# violates `require-parameter-annotation`: one parameter is missing an annotation
def add(a, b: int) -> int:
    """Add `a` and `b`."""
    return a + b


# violates `require-parameter-annotation`: you need annotations even if you have default
# values
def double(a=1) -> int:
    """Return the input multiplied by `2`."""
    return a * 2


# violates `require-parameter-annotation`: methods also need to have their parameters
# annotated
class Calculator:
    """A device for doing some math."""

    def add(self, a, b: int) -> int:
        """Add `a` and `b` using this calculator."""
        return self.calculate("+", a, b)


# no violation: all parameters annotated; note that `self` and `cls` do not require
# annotations
class Keyboard:
    """A device most programmers use."""

    def repeat_keys(self, keys: str, times: int) -> int:
        """Return the keys in `keys` repeated `times` times."""
        return keys * times

    @classmethod
    def from_company(cls, company_name: str, model: str) -> "Keyboard":
        """Purchase a keyboard of model `model` from company `company_name`."""
        company = Company.from_name(company_name)
        keyboard_model = company.keyboards[model]
        return keyboard_model()


# violate `require-return-annotation`: the function has its parameters correctly
# annotated, but not the return value
def multiply(a: int, b: int):
    """Multiply `a` and `b`."""
    return a * b


def fourty_three():
    """The answer to most questions, plus one."""
    return 43


# no violation: all parameters and return value annotated 🎉
def repeat_word(word: str, times: int) -> str:
    """The word `word` repeated `times` times."""
    return word * times


# no violation: if you have no parameters, you need no parameter annotations ;)
def fourty_two() -> int:
    """The answer to most of your questions."""
    return 42


# no violation: internal functions or protected methods (that is, functions and methods
# whose names start with an underscore) are not required to be annotated
def _add(a, b):
    return a + b
