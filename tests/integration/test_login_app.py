"""!
@file test_login_app.py
@brief Integration tests of the login form app, using the Flask test client.
"""

import re

import pytest
from flask.testing import FlaskClient

from html_forms import constants
from html_forms.presentation.features.login.app import create_app


@pytest.fixture
def client() -> FlaskClient:
    """!@brief A test client for a fresh app."""
    return create_app().test_client()


def test_home_serves_form_when_get(client: FlaskClient) -> None:
    """!@brief GET / returns an h1 and a form posting name and password."""
    response = client.get(constants.ROUTE_HOME)
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "<h1>" in html
    assert f'action="{constants.ROUTE_LOGIN}"' in html
    assert 'method="post"' in html
    assert f'name="{constants.FIELD_NAME}"' in html
    assert f'name="{constants.FIELD_PASSWORD}"' in html


def test_login_returns_values_when_posted(client: FlaskClient) -> None:
    """!@brief POST /login echoes the submitted name and password in an h1."""
    response = client.post(
        constants.ROUTE_LOGIN,
        data={constants.FIELD_NAME: "Ada", constants.FIELD_PASSWORD: "secret"},
    )
    assert response.status_code == 200
    assert response.get_data(as_text=True) == ("<h1>Name: Ada, Password: secret</h1>")


def test_login_is_not_allowed_when_get(client: FlaskClient) -> None:
    """!@brief GET /login is refused with 405."""
    assert client.get(constants.ROUTE_LOGIN).status_code == 405


def test_login_escapes_html_when_values_contain_markup(client: FlaskClient) -> None:
    """!@brief Markup in submitted values is escaped."""
    response = client.post(
        constants.ROUTE_LOGIN,
        data={
            constants.FIELD_NAME: "<script>x</script>",
            constants.FIELD_PASSWORD: "a&b",
        },
    )
    html = response.get_data(as_text=True)
    assert "<script>" not in html
    assert "&lt;script&gt;" in html
    assert "a&amp;b" in html


def test_login_uses_empty_values_when_fields_missing(client: FlaskClient) -> None:
    """!@brief Missing fields give 200 with empty values."""
    response = client.post(constants.ROUTE_LOGIN, data={})
    assert response.status_code == 200
    assert re.fullmatch(r"<h1>Name: , Password: </h1>", response.get_data(as_text=True))
