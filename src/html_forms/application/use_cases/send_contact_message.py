"""!
@file send_contact_message.py
@brief Use case: send a contact form message by mail.
"""

from html_forms.application.ports.mail_sender import MailSender
from html_forms.domain.entities.contact_message import ContactMessage


def send_contact_message(sender: MailSender, message: ContactMessage) -> None:
    """!
    @brief Send a contact message.
    @param sender Mail port used to deliver it.
    @param message The message from the visitor.
    @throws MailDeliveryError when it could not be delivered.
    """
    sender.send(message)
