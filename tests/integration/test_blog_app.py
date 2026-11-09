"""!
@file test_blog_app.py
@brief Integration tests of the blog and its contact form (Flask test client).
"""

import logging
import re
from pathlib import Path

import pytest
from flask.testing import FlaskClient

from html_forms import constants
from html_forms.domain.entities.contact_message import ContactMessage
from html_forms.domain.errors.mail_delivery_error import MailDeliveryError
from html_forms.presentation.features.blog.app import create_app

FORM_DATA = {
    constants.FIELD_NAME: "Zed Secretname",
    constants.FIELD_EMAIL: "zed.secret@example.invalid",
    constants.FIELD_PHONE: "+45 5550 1234",
    constants.FIELD_MESSAGE: "Private words nobody should log",
}


class FakeMailSender:
    """!@brief Fake of the MailSender port; fails when told to."""

    def __init__(self, fail: bool = False) -> None:
        """!
        @brief Create the fake.
        @param fail True to raise MailDeliveryError on send.
        """
        self.received: list[ContactMessage] = []
        self._fail = fail

    def send(self, message: ContactMessage) -> None:
        """!
        @brief Record the message or fail.
        @param message The message.
        @throws MailDeliveryError when created with fail=True.
        """
        if self._fail:
            raise MailDeliveryError("down: " + message.email)
        self.received.append(message)


@pytest.fixture
def sender() -> FakeMailSender:
    """!
    @brief The fake mail sender of the app under test.
    @return The fake.
    """
    return FakeMailSender()


@pytest.fixture
def client(sender: FakeMailSender) -> FlaskClient:
    """!
    @brief Test client of a fresh blog app with a fake mail sender.
    @param sender The fake mail sender.
    @return The client.
    """
    return create_app(mail_sender=sender).test_client()


@pytest.mark.parametrize(
    "path", [constants.ROUTE_HOME, constants.ROUTE_ABOUT, constants.ROUTE_CONTACT]
)
def test_page_get_returns_200(client: FlaskClient, path: str) -> None:
    """!@brief Home, about and contact render."""
    assert client.get(path).status_code == 200


def test_home_links_to_every_post(client: FlaskClient) -> None:
    """!@brief The home page links each of the three posts."""
    html = client.get(constants.ROUTE_HOME).get_data(as_text=True)
    for post_id in (1, 2, 3):
        assert f'href="/post/{post_id}"' in html


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_post_page_returns_200(client: FlaskClient, post_id: int) -> None:
    """!@brief Each bundled post has a page."""
    assert client.get(f"/post/{post_id}").status_code == 200


def test_post_page_returns_404_when_unknown(client: FlaskClient) -> None:
    """!@brief An unknown post id gives 404."""
    assert client.get("/post/999").status_code == 404


def test_stylesheet_is_served(client: FlaskClient) -> None:
    """!@brief The local CSS is reachable, so the page works offline."""
    assert client.get("/static/css/blog.css").status_code == 200


def test_form_entry_returns_success_heading(client: FlaskClient) -> None:
    """!@brief POST /form-entry returns the first-version string."""
    response = client.post(constants.ROUTE_FORM_ENTRY, data=FORM_DATA)
    assert response.get_data(as_text=True) == "<h1>Successfully sent your message</h1>"


def test_form_entry_rejects_get(client: FlaskClient) -> None:
    """!@brief /form-entry accepts POST only."""
    assert client.get(constants.ROUTE_FORM_ENTRY).status_code == 405


def test_contact_post_shows_success_message(client: FlaskClient) -> None:
    """!@brief POST /contact renders the success heading."""
    response = client.post(constants.ROUTE_CONTACT, data=FORM_DATA)
    assert response.status_code == 200
    assert constants.MSG_SENT_TEXT in response.get_data(as_text=True)


def test_contact_get_does_not_show_success_message(client: FlaskClient) -> None:
    """!@brief GET /contact shows the form heading only."""
    html = client.get(constants.ROUTE_CONTACT).get_data(as_text=True)
    assert constants.MSG_SENT_TEXT not in html
    assert "Contact Me" in html


def test_contact_form_posts_to_contact_with_named_fields(
    client: FlaskClient,
) -> None:
    """!@brief The form posts to /contact and has the four named fields."""
    html = client.get(constants.ROUTE_CONTACT).get_data(as_text=True)
    form = re.search(r"<form[^>]*>", html)
    assert form is not None
    assert 'method="post"' in form.group(0)
    assert 'action="/contact"' in form.group(0)
    for field in constants.CONTACT_FIELDS:
        assert f'name="{field}"' in html


def test_contact_escapes_html_in_submitted_values(client: FlaskClient) -> None:
    """!@brief Submitted markup is never echoed unescaped."""
    payload = "<script>alert(1)</script>"
    data = {**FORM_DATA, constants.FIELD_MESSAGE: payload}
    html = client.post(constants.ROUTE_CONTACT, data=data).get_data(as_text=True)
    assert payload not in html


@pytest.mark.parametrize("path", [constants.ROUTE_CONTACT, constants.ROUTE_FORM_ENTRY])
def test_submission_does_not_leak_personal_data(
    client: FlaskClient,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
    path: str,
) -> None:
    """!@brief Submitted values appear neither in logs nor on stdout/stderr."""
    with caplog.at_level(logging.DEBUG):
        client.post(path, data=FORM_DATA)
    captured = capsys.readouterr()
    output = caplog.text + captured.out + captured.err
    for value in FORM_DATA.values():
        assert value not in output
    assert "message_length" in caplog.text


def test_contact_post_passes_the_four_values_to_the_mail_sender(
    client: FlaskClient, sender: FakeMailSender
) -> None:
    """!@brief The sender receives name, email, phone and message."""
    client.post(constants.ROUTE_CONTACT, data=FORM_DATA)
    assert sender.received == [
        ContactMessage(
            FORM_DATA[constants.FIELD_NAME],
            FORM_DATA[constants.FIELD_EMAIL],
            FORM_DATA[constants.FIELD_PHONE],
            FORM_DATA[constants.FIELD_MESSAGE],
        )
    ]


def test_contact_post_returns_502_when_delivery_fails() -> None:
    """!@brief A failing sender gives 502, an error text and no success heading."""
    client = create_app(mail_sender=FakeMailSender(fail=True)).test_client()
    response = client.post(constants.ROUTE_CONTACT, data=FORM_DATA)
    html = response.get_data(as_text=True)
    assert response.status_code == constants.HTTP_BAD_GATEWAY
    assert constants.MAIL_DELIVERY_FAILED_TEXT in html
    assert constants.MSG_SENT_TEXT not in html


def test_contact_post_returns_400_when_email_has_line_break(
    client: FlaskClient, sender: FakeMailSender
) -> None:
    """!@brief CRLF in the email is refused and nothing is sent."""
    data = {**FORM_DATA, constants.FIELD_EMAIL: "a@x.invalid\r\nBcc: e@x.invalid"}
    response = client.post(constants.ROUTE_CONTACT, data=data)
    html = response.get_data(as_text=True)
    assert response.status_code == constants.HTTP_BAD_REQUEST
    assert constants.CONTACT_INVALID_TEXT in html
    assert constants.MSG_SENT_TEXT not in html
    assert sender.received == []


def test_contact_post_returns_400_when_message_is_empty(
    client: FlaskClient,
) -> None:
    """!@brief A blank message is refused."""
    data = {**FORM_DATA, constants.FIELD_MESSAGE: "   "}
    response = client.post(constants.ROUTE_CONTACT, data=data)
    assert response.status_code == constants.HTTP_BAD_REQUEST


def test_contact_post_returns_502_when_mail_is_not_configured(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """!@brief Without MAIL_HOST and MAIL_RECIPIENT the default sender fails."""
    monkeypatch.delenv(constants.ENV_MAIL_HOST, raising=False)
    monkeypatch.delenv(constants.ENV_MAIL_RECIPIENT, raising=False)
    response = create_app().test_client().post(constants.ROUTE_CONTACT, data=FORM_DATA)
    assert response.status_code == constants.HTTP_BAD_GATEWAY


def test_delivery_failure_log_has_no_personal_data(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """!@brief A failed send logs the exception class name only."""
    client = create_app(mail_sender=FakeMailSender(fail=True)).test_client()
    with caplog.at_level(logging.DEBUG):
        client.post(constants.ROUTE_CONTACT, data=FORM_DATA)
    assert "MailDeliveryError" in caplog.text
    for value in FORM_DATA.values():
        assert value not in caplog.text


def test_no_source_file_reads_a_dotenv_file() -> None:
    """!@brief No file under src/ mentions a .env file."""
    src = Path(__file__).resolve().parents[2] / "src"
    pattern = re.compile(r"\.env(?!\w)")
    offenders = [
        str(path)
        for path in src.rglob("*")
        if path.is_file()
        and path.suffix != ".pyc"
        and pattern.search(path.read_text(encoding="utf-8", errors="ignore"))
    ]
    assert offenders == []
