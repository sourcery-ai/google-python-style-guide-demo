# violation of `docstrings-for-modules`: docstrings are triple-quoted strings, not
# comments.
# A module docstring should appear here, right at the top of the file.
# The other files in this individual rule examples directory correctly contain module
# docstrings.

# ----------------------------------------------------------------------------------
# [3.8 Docstring and Comment Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#38-docstring-and-comment-rules)
# ----------------------------------------------------------------------------------
#
# This example file contains pieces of code that either comply with or violate the
# rules `docstrings-for-classes`, `docstrings-for-functions` and
# `docstrings-for-modules`.
#
# Take a look at the top of this file: there is already a violation there.

# violations of `docstrings-for-classes`
class CheeseShopAddress:
    ...


class CheeseShopAddress(Address):
    ...


class OutOfCheeseError(Exception):
    def __str__(self):
        """Well, at least this method has a docstring."""
        return "Would you rather have some spam?"


# no violations: the following classes contain docstrings
class CheeseShopAddress:
    """The address of a cheese shop."""


class OutOfCheeseError(Exception):
    """No more cheese is available."""
    def __str__(self):
        """Suggest alternative food."""
        return "Would you rather have some spam?"


# no violation: internal classes (marked by a leading underscore) are not required to
# have docstrings
class _BrieCounter:
    limit: 500


# violation of `docstrings-for-functions`: public functions should always be documented
def grow(plant: Plant) -> None:
    assert plant.is_alive()
    plant.height += 1


# no violation: internal functions (that is, functions starting with an underscore) are
# not required to have docstrings if they are small enough
def _grow(plant: Plant) -> None:
    assert plant.is_alive()
    plant.height += 1


# violation of `docstrings-for-functions`: even internal functions should be documented
# if they are too complex
def _plant_and_grow(plant: Plant) -> None:
    pot = plant.owner.get_empty_pot()
    pot.contents.add("soil", fraction=0.5)
    pot.contents.add(plant, orientation="vertical")

    type_of_plant = plant.__class__
    for day in range(0, type_of_plant.gestation_time, type_of_plant.watering_interval):
        print("Watering plant on day", day)
        pot.contents.add("water", amount="200ml")


# no violation: methods also have to be documented, including `__dunder__` methods
class Gardner:
    """A person that tends a garden. """

    def __init__(self, name: str, favorite_plant: Plant) -> None:
        """Give this gardner a name and choose their favorite plant."""
        self.name = name
        self.favorite_plant = favorite_plant

    def sow_the_seeds_of_love(self) -> None:
        """Sow the seeds of love."""
        for seed in self.storage.all_seeds:
            if isinstance(seed, SeedOfLove):
                self.sow(seed)


# no violation: nested functions do not need docstrings
def fight(plant: Plant, zombies: list[Zombie]) -> None:
    """Plants and zombies should fight."""

    def _fight_one(plant: Plant, zombie: Zombie) -> None:
        plant.attack(zombie)
        zombie.attack(plant)

    for zombie in zombies:
        _fight_one(plant, zombie)
