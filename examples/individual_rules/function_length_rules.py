"""
----------------------------------------------------------------------------------
[3.18 Function Length Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#318-function-length-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rule `no-long-functions`.
"""

# no violation: short functions are easier to understand and work with
def count_to_forty_short() -> None:
    """Count from one to 42."""
    for i in range(1, 43):
        print(i)


# violate `no-long-functions`: long functions are harder to maintain and to reason about
def count_to_forty_long() -> None:
    """Count from one to 42."""
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)
    print(10)
    print(11)
    print(12)
    print(13)
    print(14)
    print(15)
    print(16)
    print(17)
    print(18)
    print(19)
    print(20)
    print(21)
    print(22)
    print(23)
    print(24)
    print(25)
    print(26)
    print(27)
    print(28)
    print(29)
    print(30)
    print(31)
    print(32)
    print(33)
    print(34)
    print(35)
    print(36)
    print(37)
    print(38)
    print(39)
    print(40)
    print(41)
    print(42)
