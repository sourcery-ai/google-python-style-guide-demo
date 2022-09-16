"""
----------------------------------------------------------------------------------
[2.5 Global Variable Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#25-global-variable-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
global variable rule `avoid-global-variables`.
"""

# violates `avoid-global-variables` because it is named like a variable, and not a
# constant
max_holy_handgrenade_count = 3

# violates `avoid-global-variables` as well - type annotations are supported
max_holy_handgrenade_count: int = 3

# no violation: this is not defining a new variable, but instead setting an item
holy_handgrenade[1] = 3

# no violation: this variable is marked as internal to its module
_max_holy_handgrenade_count = 3

# no violation: this is a type alias defined in UpperCamelCase
HolyGrenades = Dict[str, Grenade]

# no violation: this is a top-level constant named in UPPER_CASE
MAX_HOLY_HANDGRENADE_COUNT = 3

# no violation: variables are OK when not at the module-level (in this example, it is in
# the body of a function)
def throw_grenades() -> None:
    """Can I have some variables, please?"""
    max_holy_handgrenade_count = 3
