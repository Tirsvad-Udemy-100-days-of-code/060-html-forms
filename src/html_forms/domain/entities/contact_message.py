"""!
@file contact_message.py
@brief The ContactMessage entity: what a visitor sends through the contact form.
"""

from dataclasses import dataclass

from html_forms import constants
from html_forms.domain.errors.invalid_contact_message_error import (
    InvalidContactMessageError,
)

_HEADER_FIELDS = ("name", "email", "phone")


@dataclass(frozen=True, slots=True)
class ContactMessage:
    """!
    @brief One message from the contact form.

    Surrounding whitespace is stripped. Name, email and phone end up in email
    headers, so a CR or LF in them is rejected (header injection guard).
    @param name Name of the sender.
    @param email Email address of the sender.
    @param phone Phone number of the sender.
    @param message Text of the message; not empty.
    """

    name: str
    email: str
    phone: str
    message: str

    def __post_init__(self) -> None:
        """!
        @brief Strip the fields and check the rules.
        @throws InvalidContactMessageError when a rule is broken.
        """
        object.__setattr__(self, "name", self.name.strip())
        object.__setattr__(self, "email", self.email.strip())
        object.__setattr__(self, "phone", self.phone.strip())
        object.__setattr__(self, "message", self.message.strip())
        for field in _HEADER_FIELDS:
            value: str = getattr(self, field)
            if any(char in value for char in constants.LINE_BREAK_CHARACTERS):
                raise InvalidContactMessageError(f"{field} contains a line break")
        if not self.message:
            raise InvalidContactMessageError("message is empty")
