"""
----------------------------------------------------------------------------------
[2.17 Decorator Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#217-decorator-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
rule `do-not-use-staticmethod`.
"""

class EventRecommender:
    """Recommend events to users."""

    # violation of `do-not-use-staticmethod`
    @staticmethod
    def get_suggested_event_from_default_recommender() -> str:
        """What about watching Monty Python?"""
        return (
            EventRecommender.default_instance()
            .all_events.sortby(lambda event: event.score)
            .first()
        )

    # no violation: no decorators :)
    def get_suggested_event_from_current_recommender(self) -> str:
        """What about watching Monty Python... again?"""
        return self.all_events.sortby(lambda event: event.score).first()

    # no violation: other decorators are OK
    @send_email_as_well
    def get_suggested_event_from_current_recommender_and_send_email(self) -> str:
        """What about watching Monty Python... again?"""
        return self.all_events.sortby(lambda event: event.score).first()
