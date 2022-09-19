"""
----------------------------------------------------------------------------------
[3.15 Getter and Setter Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#315-getter-and-setter-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rule `avoid-trivial-properties`.
"""

# violation of `avoid-trivial-properties` because the property `name` only reads from or
# writes to an attribute without any extra logic
class Student:
    """A person that studies."""

    @property
    def name(self) -> str:
        """Get the name of this student"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of this student"""
        self._name = new_name


# no violation: the following class's `name` property is not trivial because it does not
# contain an associated setter. You can use this pattern to "ensure" that an attribute
# is read-only
class Student:
    """A person that studies."""

    @property
    def name(self) -> str:
        """Get the name of this student"""
        return self._name


# no violation: the following class's `name` property is not trivial because the getter
# method contains extra logic that is not simply returning an attribute
class Student:
    """A person that studies."""

    @property
    def name(self) -> str:
        """Get the name of this student"""
        return self._name.title()

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of this student"""
        self._name = new_name


# no violation: the following class's `name` property is not trivial because the setter
# method contains extra logic that is not simply returning an attribute
class Student:
    """A person that studies."""

    @property
    def name(self) -> str:
        """Get the name of this student"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of this student"""
        old_name = self._name
        self._name = new_name

        db = get_student_db()
        db.replace(old_name, new_name)
