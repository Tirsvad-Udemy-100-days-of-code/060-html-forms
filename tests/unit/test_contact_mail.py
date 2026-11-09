"""!
@file test_contact_mail.py
@brief Unit tests of ContactMessage, the send use case, the SMTP settings and
the SMTP mail sender (no network: smtplib.SMTP is replaced by a fake).
"""

import smtplib
from email.message import EmailMessage
from types import TracebackType
from typing import Self

import pytest

from html_forms import constants
from html_forms.application.use_cases.send_contact_message import (
    send_contact_message,
)
from html_forms.domain.entities.contact_message import ContactMessage
from html_forms.domain.errors.invalid_contact_message_error import (
    InvalidContactMessageError,
)
from html_forms.domain.errors.mail_delivery_error import MailDeliveryError
from html_forms.infrastructure.config.mail_settings import SmtpSettings
from html_forms.infrastructure.mail.smtp_mail_sender import SmtpMailSender
from html_forms.infrastructure.mail.unconfigured_mail_sender import (
    UnconfiguredMailSender,
)

MESSAGE = ContactMessage("Ann", "ann@example.invalid", "+45 1234", "Hello there")


class FakeMailSender:
    """!@brief Fake of the MailSender port that records what it receives."""

    def __init__(self) -> None:
        """!@brief Start with nothing received."""
        self.received: list[ContactMessage] = []

    def send(self, message: ContactMessage) -> None:
        """!
        @brief Record the message.
        @param message The message.
        """
        self.received.append(message)


class FakeSmtp:
    """!@brief Stand-in for smtplib.SMTP that records the calls made on it."""

    calls: list[str] = []
    sent: list[EmailMessage] = []
    connect_args: list[tuple[str, int, float]] = []
    failure: Exception | None = None

    def __init__(self, host: str, port: int, timeout: float) -> None:
        """!
        @brief Record the connection arguments.
        @param host Server host.
        @param port Server port.
        @param timeout Timeout in seconds.
        """
        FakeSmtp.connect_args.append((host, port, timeout))

    def __enter__(self) -> Self:
        """!
        @brief Enter the with block.
        @return This object.
        """
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        """!
        @brief Leave the with block.
        @param exc_type Exception type.
        @param exc Exception.
        @param tb Traceback.
        """
        FakeSmtp.calls.append("quit")

    def starttls(self) -> None:
        """!@brief Record STARTTLS."""
        FakeSmtp.calls.append("starttls")

    def login(self, user: str, password: str) -> None:
        """!
        @brief Record the login.
        @param user User.
        @param password Password.
        """
        FakeSmtp.calls.append(f"login:{user}:{password}")

    def send_message(self, message: EmailMessage) -> None:
        """!
        @brief Record the email, or fail when a failure is set.
        @param message The email.
        """
        FakeSmtp.calls.append("send_message")
        if FakeSmtp.failure is not None:
            raise FakeSmtp.failure
        FakeSmtp.sent.append(message)


@pytest.fixture
def fake_smtp(monkeypatch: pytest.MonkeyPatch) -> type[FakeSmtp]:
    """!
    @brief Replace smtplib.SMTP with a clean FakeSmtp.
    @param monkeypatch The pytest monkeypatch fixture.
    @return The fake class.
    """
    FakeSmtp.calls = []
    FakeSmtp.sent = []
    FakeSmtp.connect_args = []
    FakeSmtp.failure = None
    monkeypatch.setattr(smtplib, "SMTP", FakeSmtp)
    return FakeSmtp


def _settings(user: str = "", use_tls: bool = False) -> SmtpSettings:
    """!
    @brief Build SMTP settings for tests.
    @param user Login user; empty for none.
    @param use_tls Whether to use STARTTLS.
    @return The settings.
    """
    return SmtpSettings(
        "smtp.example.invalid", 2525, user, "pw", "me@x.invalid", use_tls
    )


# ContactMessage


def test_contact_message_strips_surrounding_whitespace() -> None:
    """!@brief Every field is stripped."""
    message = ContactMessage("  Ann ", " a@x.invalid ", " 1 ", "\n hi \n")
    assert message == ContactMessage("Ann", "a@x.invalid", "1", "hi")


@pytest.mark.parametrize("field", ["name", "email", "phone"])
@pytest.mark.parametrize("bad", ["a\r\nBcc: evil@x.invalid", "a\nb", "a\rb"])
def test_contact_message_rejects_line_break_in_header_field(
    field: str, bad: str
) -> None:
    """!@brief CR or LF inside name, email or phone is refused."""
    values = {"name": "n", "email": "e@x.invalid", "phone": "1", "message": "m"}
    values[field] = bad
    with pytest.raises(InvalidContactMessageError):
        ContactMessage(**values)


@pytest.mark.parametrize("text", ["", "   ", "\n\t"])
def test_contact_message_rejects_empty_message(text: str) -> None:
    """!@brief An empty or blank message is refused."""
    with pytest.raises(InvalidContactMessageError):
        ContactMessage("n", "e@x.invalid", "1", text)


def test_contact_message_allows_line_breaks_inside_message() -> None:
    """!@brief The body may be multi-line."""
    assert ContactMessage("n", "e@x.invalid", "1", "a\nb").message == "a\nb"


def test_invalid_error_does_not_contain_submitted_value() -> None:
    """!@brief The error names the rule, not the value."""
    with pytest.raises(InvalidContactMessageError) as error:
        ContactMessage("n", "secret@x.invalid\nBcc: z", "1", "m")
    assert "secret" not in str(error.value)


# Use case


def test_send_contact_message_passes_message_to_sender() -> None:
    """!@brief The use case hands the message to the port."""
    sender = FakeMailSender()
    send_contact_message(sender, MESSAGE)
    assert sender.received == [MESSAGE]


# Settings


def _environ(**extra: str) -> dict[str, str]:
    """!
    @brief Environment with a host and a recipient plus extras.
    @param extra Additional variables.
    @return The environment.
    """
    base = {
        constants.ENV_MAIL_HOST: "smtp.example.invalid",
        constants.ENV_MAIL_RECIPIENT: "me@x.invalid",
    }
    return {**base, **extra}


def test_settings_use_defaults() -> None:
    """!@brief Port 587 and STARTTLS on when only host and recipient are set."""
    settings = SmtpSettings.from_environ(_environ())
    assert settings == SmtpSettings(
        "smtp.example.invalid", 587, "", "", "me@x.invalid", True
    )


def test_settings_read_all_values() -> None:
    """!@brief Every variable is honoured."""
    settings = SmtpSettings.from_environ(
        _environ(
            **{
                constants.ENV_MAIL_PORT: "2525",
                constants.ENV_MAIL_USER: "u",
                constants.ENV_MAIL_PASSWORD: "p",
            }
        )
    )
    assert settings == SmtpSettings(
        "smtp.example.invalid", 2525, "u", "p", "me@x.invalid", True
    )


@pytest.mark.parametrize(
    "missing", [constants.ENV_MAIL_HOST, constants.ENV_MAIL_RECIPIENT]
)
def test_settings_none_when_host_or_recipient_missing(missing: str) -> None:
    """!@brief Without host or recipient there are no settings."""
    environ = _environ()
    del environ[missing]
    assert SmtpSettings.from_environ(environ) is None


def test_settings_none_when_environment_empty() -> None:
    """!@brief An empty environment gives None."""
    assert SmtpSettings.from_environ({}) is None


@pytest.mark.parametrize("value", ["false", "FALSE", "0"])
def test_settings_tls_can_be_disabled(value: str) -> None:
    """!@brief MAIL_USE_TLS false or 0 switches STARTTLS off."""
    settings = SmtpSettings.from_environ(
        _environ(**{constants.ENV_MAIL_USE_TLS: value})
    )
    assert settings is not None
    assert settings.use_tls is False


@pytest.mark.parametrize("value", ["true", "1", "yes"])
def test_settings_tls_stays_on_for_other_values(value: str) -> None:
    """!@brief Any other MAIL_USE_TLS value keeps STARTTLS on."""
    settings = SmtpSettings.from_environ(
        _environ(**{constants.ENV_MAIL_USE_TLS: value})
    )
    assert settings is not None
    assert settings.use_tls is True


# SmtpMailSender


def test_smtp_sender_starttls_then_login_then_send(fake_smtp: type[FakeSmtp]) -> None:
    """!@brief A configured sender secures, logs in and sends, in that order."""
    SmtpMailSender(_settings(user="u", use_tls=True)).send(MESSAGE)
    assert fake_smtp.calls == ["starttls", "login:u:pw", "send_message", "quit"]
    assert fake_smtp.connect_args == [
        ("smtp.example.invalid", 2525, constants.SMTP_TIMEOUT_SECONDS)
    ]


def test_smtp_sender_skips_starttls_and_login_when_not_configured(
    fake_smtp: type[FakeSmtp],
) -> None:
    """!@brief No TLS and no user: only the send happens."""
    SmtpMailSender(_settings()).send(MESSAGE)
    assert fake_smtp.calls == ["send_message", "quit"]


def test_smtp_sender_builds_the_email(fake_smtp: type[FakeSmtp]) -> None:
    """!@brief Headers and body carry the four fields."""
    SmtpMailSender(_settings()).send(MESSAGE)
    assert len(fake_smtp.sent) == 1
    email = fake_smtp.sent[0]
    assert email[constants.MAIL_HEADER_SUBJECT] == constants.MAIL_SUBJECT
    assert email[constants.MAIL_HEADER_TO] == "me@x.invalid"
    assert email[constants.MAIL_HEADER_FROM] == "me@x.invalid"
    assert email[constants.MAIL_HEADER_REPLY_TO] == "ann@example.invalid"
    body = email.get_content()
    assert "Name: Ann" in body
    assert "Email: ann@example.invalid" in body
    assert "Phone Number: +45 1234" in body
    assert "Message: Hello there" in body


def test_smtp_sender_uses_user_as_from(fake_smtp: type[FakeSmtp]) -> None:
    """!@brief From is the login user when there is one."""
    SmtpMailSender(_settings(user="bot@x.invalid")).send(MESSAGE)
    assert fake_smtp.sent[0][constants.MAIL_HEADER_FROM] == "bot@x.invalid"


def test_smtp_sender_maps_smtp_exception(fake_smtp: type[FakeSmtp]) -> None:
    """!@brief An SMTPException becomes MailDeliveryError with the cause kept."""
    fake_smtp.failure = smtplib.SMTPRecipientsRefused({})
    with pytest.raises(MailDeliveryError) as error:
        SmtpMailSender(_settings()).send(MESSAGE)
    assert isinstance(error.value.__cause__, smtplib.SMTPException)


def test_smtp_sender_maps_connection_refused(monkeypatch: pytest.MonkeyPatch) -> None:
    """!@brief A refused connection becomes MailDeliveryError."""

    def refuse(*args: object, **kwargs: object) -> None:
        raise ConnectionRefusedError

    monkeypatch.setattr(smtplib, "SMTP", refuse)
    with pytest.raises(MailDeliveryError) as error:
        SmtpMailSender(_settings()).send(MESSAGE)
    assert isinstance(error.value.__cause__, ConnectionRefusedError)


def test_unconfigured_sender_always_fails() -> None:
    """!@brief The null sender refuses with a clear text."""
    with pytest.raises(MailDeliveryError, match="mail is not configured"):
        UnconfiguredMailSender().send(MESSAGE)
