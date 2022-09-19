"""
----------------------------------------------------------------------------------
[2.4 Exception Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#24-exception-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
exception rule `errors-named-error`.
"""

# violation of `errors-named-error` because `Foo` inherits from a built-in exception
# type, and hence should have its name ending in `Error`
class Foo(ValueError):
    """I should be named FooError."""


# violation of `errors-named-error` because `CustomError` is assumed to be an exception
# since its name ends in `Error`, and hence `ExampleException` should end in `Error` as
# well
class ExampleException(CustomError):
    """I should be named ExampleError."""
    def __init__(self, msg: str) -> None:
        ...


# violations of `errors-named-error` because `Exception` and `BaseException` are also
# exception types
class InvalidName(Exception):
    """I should be named InvalidNameError."""


class InvalidName(BaseException):
    """I should be named InvalidNameError."""


# no violations: the derived classes' names end in `Error`
class MyError(Exception):
    """Yay, my name is great!"""
    def __init__(self, msg: str) -> None:
        ...


class NameError(AttributeError):
    """Yay, my name is great!"""


# no violation: the base class is not an exception type
class Dog(Mammal):
    """Dogs are not exceptions."""
