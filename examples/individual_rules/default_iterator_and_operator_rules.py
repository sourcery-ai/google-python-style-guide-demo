"""
----------------------------------------------------------------------------------
[2.8 Default Iterator and Operator Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#28-default-iterator-and-operator-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rule `do-not-use-has-key`. Also note that `do-not-use-has-key` has a replacement,
and hence Sourcery can automatically fix it.
"""

# violate the rule `do-not-use-has-key`
def is_week_day() -> bool:
    """Check if today is a week day by checking if "work" is one of today's tasks."""
    tasks_for_today: dict[str, Task] = get_tasks("today")

    # should be `"work" in tasks_for_today`
    is_week_day = tasks_for_today.has_key("work")


    print("Time to work!" if is_week_day else "Time to relax!")
    return is_week_day


def is_movie_in_database(movie: Movie, movies: Dict[Movie, MovieSpec]) -> bool:
    """Check if `movie` is in the database of `movies`."""

    # should be `movie in movies`
    return movies.has_key(movie)


def prompt_for_pro_subscription(database: Database) -> None:
    """Prompt the current user to subscribe to a PRO license."""
    pro_users = {
        user.name: user
        for user in database.fetch(User)
        if user.subscription == "PRO"
    }
    if pro_users.has_key(get_current_user().name):
        print("You've signed in under the PRO subscription")
    else:
        print("Please sign up for PRO to use this awesome feature!")


# no violation: `random_object` is not necessarily a dictionary, and hence the rule
# `do-not-use-has-key` is not applied
def is_random_key_in_random_object(random_key: Any, random_object: Any) -> bool:
    """Check if a random key is in a random object - not necessarily a `dict`."""
    # Not sure of `random_object` is a dictionary
    return random_object.has_key(random_key)


# no violation: the `database` object of type `Database` is not necessarily a
# dictionary, and hence the rule `do-not-use-has-key` is not applied
def has_dinos() -> bool:
    """Check if we have a dinosaur in our database. Hopefully we do!"""
    # Custom type `Database` is not a dictionary
    database: Database = get_database()
    return database.has_key("dinosaur")
