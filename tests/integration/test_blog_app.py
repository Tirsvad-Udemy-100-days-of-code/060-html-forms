"""!
@file test_blog_app.py
@brief Integration tests of the blog and its contact form (Flask test client).
"""

import logging
import re

import pytest
from flask.testing import FlaskClient

from html_forms import constants
from html_forms.presentation.features.blog.app import create_app

FORM_DATA = {
    constants.FIELD_NAME: "Zed Secretname",
    constants.FIELD_EMAIL: "zed.secret@example.invalid",
    constants.FIELD_PHONE: "+45 5550 1234",
    constants.FIELD_MESSAGE: "Private words nobody should log",
}


@pytest.fixture
def client() -> FlaskClient:
    """!
    @brief Test client of a fresh blog app.
    @return The client.
    """
    return create_app().test_client()


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
