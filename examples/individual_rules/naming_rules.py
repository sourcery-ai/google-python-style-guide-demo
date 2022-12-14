"""
----------------------------------------------------------------------------------
[3.16 Naming Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#316-naming-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rules `avoid-single-character-names-variables`,
`avoid-single-character-names-functions`, `name-type-suffix`,
`snake-case-variable-declarations`, `snake-case-arguments`, `snake-case-functions`
and `upper-camel-case-classes`.
"""

# violation of `avoid-single-character-names-variables`: and it violates it twice!
def generate_the_answer() -> int:
    """Generate the answer to most questions asked by mankind."""
    x = 0
    D = multiply(1, 2)
    return (x + 21) * D


# no violation
def generate_the_answer_but_now_with_better_names() -> int:
    """Generate the answer to most questions asked by mankind."""
    zero = 0
    two = multiply(1, 2)
    return (zero + 21) * two


# no violation: counters can have single-character names
def count_and_print(total: int) -> Iterator[int]:
    """Count up to `total` and print the numbers."""
    for i in range(total):
        print(_number_to_text(i))
        yield i


# no violation: caught exceptions can have single-character names
def maybe_kill_dinosaurs() -> Result:
    """Try to annihilate dinosaurs, but don't complain in case of failure."""
    try:
        meteor = find_meteor(origin="between Mars and Jupiter")
    except NoMeteorAvailable as e:
        print("No meteor available. Try again in a million years or so.")
        return Failure(e)

    meteor.point_to("earth")
    meteor.set_speed(BIG_NUMBER)
    meteor.go()
    return Success("No non-avian dinosaurs remaining.")


# no violation: open files can have single-character names
def register_current_number_of_dinosaurs(dinosaur_count: int) -> None:
    """Save the current number of living dinosaurs with a timestamp."""
    with open("dinosaur_registry.csv") as f:
        f.write(f"{datetime.now()}, {dinosaurs_count}")


# no violation: type variables are alright
from typing import TypeVar

_T = TypeVar("_T")


# violation of `avoid-single-character-names-functions`
def f() -> None:
    """Do something."""

# violation of `avoid-single-character-names-functions`: async functions are supported
# too
async def f() -> None:
    """Do something, but asynchronously."""


# no violation: using descriptive names is great
def function_with_good_and_descriptive_name() -> None:
    """Do something, but with a well-named function."""


# violation of `avoid-single-character-names-functions`: this rule applies to methods as
# well
class Printer:
    """A utility class for printing and representing objects."""

    def m(self, a: int, b: float) -> str:
        """Print `a` and return representation for `b`."""
        self.print(a)
        return self.repr(b)


# no violation: all methods have good names. Well done!
class Printer:
    """A utility class for printing and representing objects."""

    def good_method(self, a: int, b: float) -> str:
        """Print `a` and return representation for `b`."""
        self.print(a)
        return self.repr(b)


# violation of `name-type-suffix`: the variable `dinosaur_list` needlessly includes its
# type `list` in its name
def print_all_dinosaurs() -> None:
    """Print the names of all dinosaurs on Earth."""
    dinosaur_list = list(earth.iter_dinos())

    for dino in dinosaur_list:
        print(dino.name)


# no violation: renaming `dinosaur_list` as `dinosaurs` is cleaner!
def print_all_dinosaurs() -> None:
    """Print the names of all dinosaurs on Earth."""
    dinosaurs = list(earth.iter_dinos())

    for dino in dinosaurs:
        print(dino.name)


# violations of `snake-case-variable-declarations`
@dataclass
class Dinosaur:
    """Class representing some of the coolest animals that have ever lived."""
    miXed: int
    UpperCamelCase: int
    UpperCamelCase42: int
    mixed_and_underScore: int
    too__many__underscores: str
    _too__many__underscores: str
    ___3_underscores_prefix: str
    double_underscore_suffix__: str


# no violation: the following variables defined with acceptable names
__version__ = "3.14"
answer_to_EVERYTHING = 42
MAXIMUM_NUMBER_OF_DINOSAURS_ALLOWED = 1234567


# no violation: the following attribute declaration also has an acceptable name
@dataclass
class Dinosaur:
    """Class representing some of the coolest animals that have ever lived."""
    name: str


# violation of `snake-case-arguments`
def placeholder(randomWord: Any) -> None:
    """The parameter `randomWord` has an ugly name."""


# violation of `snake-case-arguments`
def placeholder(randomWordWithDefault: str = "random") -> None:
    """The parameter `randomWordWithDefault` has an ugly name."""


# violation of `snake-case-arguments`
def placeholder(randomWord: Any, other: Any) -> None:
    """Parameter names must have good names even if there are others."""


# violation of `snake-case-arguments`: methods also must have well-named parameters!
class Something:
    """A class with a method whose parameter names are not `snake_case`."""
    def placeholder(self, myCamelWord: str) -> None:
        """Parameter names must have good names even in methods."""


# violation of `snake-case-arguments`
def placeholder(too__many__underscores: Any) -> None:
    """Too many underscores for a snake case name - try again."""


# violation of `snake-case-arguments`
def placeholder(double_underscore_suffix__: Any) -> None:
    """Trailing double underscores are not accepted."""


# violation of `snake-case-arguments`
def placeholder(mixed_and_underScore: Any) -> None:
    """Ooops, is that a typo?"""


# violation of `snake-case-arguments`
def placeholder(__dunder_arg__: Any) -> None:
    """Parameters with `__dunder_names__` are no good either."""


# no violation
def placeholder(nice_arg_name: str) -> None:
    """What a beautiful name! Why does Python prefer `snake_case` ?????"""


# no violation
def placeholder(nice_arg_name: str = "random") -> None:
    """Beautiful name and default value - everything is alright."""


# no violation
def placeholder(simple: bool = False) -> None:
    """There is no need to have underscores for this name to be `snake_case`."""

# no violation
def placeholder(nr: int, other_nr: int, sth_completely_different: str) -> None:
    """So many compliant parameter names!"""


# no violation
class ClassWithGoodNames:
    """Look at those method and parameter names! They are snake case ????."""
    def placeholder(self, simple: bool = False) -> None:
        """This is a method with good parameter names. You are rocking!"""


# violation of `upper-camel-case-classes`
class lowercase:
    """Nice try, but no."""


# violation of `upper-camel-case-classes`
class UPPER:
    """Why are you shouting?"""


# violation of `upper-camel-case-classes`
class snake_case:
    """We like snakes, but classes should look more like camels."""


# violation of `upper-camel-case-classes`
class UPPER_UNDERSCORE:
    """Why are you shouting again?"""


# violation of `upper-camel-case-classes`
class UpperCamelCase_WithUnderscore:
    """UpperCamelCase names should have no underscores.

    With one exception: a leading underscore is allowed.
    """


# no violations: the following classes are all named in UpperCamelCase ????
class UpperCamelCase:
    """What a beautiful name!"""


class UpperCamelCase42:
    """What a beautiful name and number!"""


class B:
    """Single-character class names are alright."""


class _PrivateUpperCamelCase123:
    """As an exception, we allow UpperCamelCase classes to have a leading underscore.

    This is because internal names are normally prepended with an underscore, making
    `PublicClass` intentionally public, and `_PrivateClass` intentionally private.
    """
