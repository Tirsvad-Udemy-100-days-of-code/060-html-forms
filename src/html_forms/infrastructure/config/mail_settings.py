"""!
@file mail_settings.py
@brief SMTP settings read from environment variables (never from a file).
"""

from collections.abc import Mapping
from dataclasses import dataclass

from html_forms import constants


@dataclass(frozen=True, slots=True)
class SmtpSettings:
    """!
    @brief Where and how to send the email.
    @param host SMTP server host name.
    @param port SMTP server port.
    @param user Login user; empty for no login.
    @param password Login password.
    @param recipient Address that receives the contact messages.
    @param use_tls True to upgrade the connection with STARTTLS.
    """

    host: str
    port: int
    user: str
    password: str
    recipient: str
    use_tls: bool

    @classmethod
    def from_environ(cls, environ: Mapping[str, str]) -> "SmtpSettings | None":
        """!
        @brief Build the settings from environment variables.
        @param environ The environment, for example os.environ.
        @return The settings, or None when the host or the recipient is missing.
        """
        host = environ.get(constants.ENV_MAIL_HOST, "").strip()
        recipient = environ.get(constants.ENV_MAIL_RECIPIENT, "").strip()
        if not host or not recipient:
            return None
        port_text = environ.get(constants.ENV_MAIL_PORT, "").strip()
        tls_text = environ.get(constants.ENV_MAIL_USE_TLS, "").strip().lower()
        return cls(
            host=host,
            port=int(port_text) if port_text else constants.DEFAULT_MAIL_PORT,
            user=environ.get(constants.ENV_MAIL_USER, ""),
            password=environ.get(constants.ENV_MAIL_PASSWORD, ""),
            recipient=recipient,
            use_tls=tls_text not in constants.MAIL_TLS_OFF_VALUES,
        )
