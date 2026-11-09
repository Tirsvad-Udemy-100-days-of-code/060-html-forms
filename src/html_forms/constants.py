"""!
@file constants.py
@brief All constants of the html-forms project in one place.

Every literal that more than one module needs (route paths, form field
names, messages, environment variable names) is defined here, once.
"""

## @brief Name of the Python package, used in logs and the page title.
APP_NAME = "html-forms"

## @brief Version of the project; keep in step with pyproject.toml.
APP_VERSION = "0.1.0"

## @brief Host the development servers listen on.
DEFAULT_HOST = "127.0.0.1"

## @brief Port of the stand-alone login form demo (lecture steps L1 to L4).
DEMO_PORT = 5000

## @brief Port of the blog with the contact form (lecture steps L5 to L9).
BLOG_PORT = 5001

## @brief Route of the home page, which serves the login form.
ROUTE_HOME = "/"

## @brief Route the login form posts to.
ROUTE_LOGIN = "/login"

## @brief Name of the name input of the login form.
FIELD_NAME = "name"

## @brief Name of the password input of the login form.
FIELD_PASSWORD = "password"

## @brief Name of the template of the login page.
TEMPLATE_LOGIN = "index.html"

## @brief Heading text of the login page.
LOGIN_HEADING = "Login"
