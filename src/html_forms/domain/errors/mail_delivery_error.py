"""!
@file mail_delivery_error.py
@brief Error raised when a message could not be delivered by mail.
"""


class MailDeliveryError(Exception):
    """!@brief The email could not be sent; the cause is chained with `from`."""
