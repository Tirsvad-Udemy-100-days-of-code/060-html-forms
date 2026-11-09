"""!
@file smtp_mail_sender.py
@brief MailSender adapter that sends through an SMTP server (smtplib).
"""

import smtplib
from email.message import EmailMessage

from html_forms import constants
from html_forms.domain.entities.contact_message import ContactMessage
from html_forms.domain.errors.mail_delivery_error import MailDeliveryError
from html_forms.infrastructure.config.mail_settings import SmtpSettings


class SmtpMailSender:
    """!@brief Sends contact messages as email through SMTP."""

    def __init__(self, settings: SmtpSettings) -> None:
        """!
        @brief Create the sender.
        @param settings SMTP server and mailbox settings.
        """
        self._settings = settings

    def send(self, message: ContactMessage) -> None:
        """!
        @brief Send the message by email.
        @param message The message to send.
        @throws MailDeliveryError when the server cannot be reached or refuses it.
        """
        email = self._build(message)
        settings = self._settings
        try:
            with smtplib.SMTP(
                settings.host, settings.port, timeout=constants.SMTP_TIMEOUT_SECONDS
            ) as connection:
                if settings.use_tls:
                    connection.starttls()
                if settings.user:
                    connection.login(settings.user, settings.password)
                connection.send_message(email)
        except (smtplib.SMTPException, OSError) as error:
            raise MailDeliveryError(type(error).__name__) from error

    def _build(self, message: ContactMessage) -> EmailMessage:
        """!
        @brief Build the email for a contact message.
        @param message The contact message.
        @return The email, with the sender in Reply-To.
        """
        settings = self._settings
        email = EmailMessage()
        email[constants.MAIL_HEADER_FROM] = settings.user or settings.recipient
        email[constants.MAIL_HEADER_TO] = settings.recipient
        email[constants.MAIL_HEADER_REPLY_TO] = message.email
        email[constants.MAIL_HEADER_SUBJECT] = constants.MAIL_SUBJECT
        email.set_content(
            f"{constants.MAIL_LABEL_NAME}: {message.name}\n"
            f"{constants.MAIL_LABEL_EMAIL}: {message.email}\n"
            f"{constants.MAIL_LABEL_PHONE}: {message.phone}\n"
            f"{constants.MAIL_LABEL_MESSAGE}: {message.message}\n"
        )
        return email
