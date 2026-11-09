"""!
@file app.py
@brief Flask app of the Day 60 login form demo.
"""

from pathlib import Path

from flask import Flask, render_template, request
from markupsafe import escape

from html_forms import constants

## @brief Folder with the templates of this feature.
TEMPLATES_DIR = Path(__file__).parent / "templates"


def home() -> str:
    """!
    @brief Serve the login form.
    @return The rendered index.html page.
    """
    return render_template(
        constants.TEMPLATE_LOGIN,
        heading=constants.LOGIN_HEADING,
        field_name=constants.FIELD_NAME,
        field_password=constants.FIELD_PASSWORD,
    )


def receive_data() -> str:
    """!
    @brief Show the submitted name and password as a heading.
    @return An h1 element with the HTML-escaped values; missing fields are empty.
    """
    name = escape(request.form.get(constants.FIELD_NAME, ""))
    password = escape(request.form.get(constants.FIELD_PASSWORD, ""))
    return f"<h1>Name: {name}, Password: {password}</h1>"


def create_app() -> Flask:
    """!
    @brief Build the Flask app and register its routes.
    @return The configured Flask application.
    """
    app = Flask(__name__, template_folder=str(TEMPLATES_DIR))
    app.add_url_rule(constants.ROUTE_HOME, view_func=home, methods=["GET"])
    app.add_url_rule(constants.ROUTE_LOGIN, view_func=receive_data, methods=["POST"])
    return app


def main() -> None:
    """!
    @brief Run the demo on the development server.
    """
    create_app().run(host=constants.DEFAULT_HOST, port=constants.DEMO_PORT)


if __name__ == "__main__":
    main()
