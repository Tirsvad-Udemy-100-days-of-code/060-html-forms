"""!
@file mail_sender.py
@brief Port: how a contact message leaves the application by mail.
"""

from typing import Protocol

from html_forms.domain.entities.contact_message import ContactMessage


class MailSender(Protocol):
    """!@brief Sends a contact message by email."""

    def send(self, message: ContactMessage) -> None:
        """!
        @brief Send the message.
        @param message The message to send.
        @throws MailDeliveryError when it could not be delivered.
        """
        ...
