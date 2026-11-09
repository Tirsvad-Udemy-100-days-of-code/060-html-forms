"""!
@file unconfigured_mail_sender.py
@brief MailSender used when no SMTP settings exist.
"""

from html_forms import constants
from html_forms.domain.entities.contact_message import ContactMessage
from html_forms.domain.errors.mail_delivery_error import MailDeliveryError


class UnconfiguredMailSender:
    """!@brief Refuses every message, so the visitor sees a clear failure."""

    def send(self, message: ContactMessage) -> None:
        """!
        @brief Always fail.
        @param message The message that cannot be sent.
        @throws MailDeliveryError always.
        """
        raise MailDeliveryError(constants.MAIL_NOT_CONFIGURED_TEXT)
