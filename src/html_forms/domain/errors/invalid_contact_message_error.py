"""!
@file invalid_contact_message_error.py
@brief Error raised when a contact message breaks a domain rule.
"""


class InvalidContactMessageError(ValueError):
    """!@brief The contact message is not acceptable."""

    def __init__(self, reason: str) -> None:
        """!
        @brief Build the error.
        @param reason Which rule failed; never the submitted value itself.
        """
        super().__init__(reason)
        self.reason = reason
