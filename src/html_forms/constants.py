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

## @brief Route of the home page of both apps (the login form and the blog).
ROUTE_HOME = "/"

## @brief Route the login form posts to.
ROUTE_LOGIN = "/login"

## @brief Name of the name input of the login form and of the contact form.
FIELD_NAME = "name"

## @brief Name of the password input of the login form.
FIELD_PASSWORD = "password"

## @brief Name of the template of the login page.
TEMPLATE_LOGIN = "index.html"

## @brief Heading text of the login page.
LOGIN_HEADING = "Login"

## @brief Route of the about page.
ROUTE_ABOUT = "/about"

## @brief Route of one post; the converter keeps ids to integers.
ROUTE_POST = "/post/<int:post_id>"

## @brief Route of the contact page and its form (GET and POST).
ROUTE_CONTACT = "/contact"

## @brief Route of the first version of the form handler (POST only).
ROUTE_FORM_ENTRY = "/form-entry"

## @brief Name of the form field with the sender's email address.
FIELD_EMAIL = "email"

## @brief Name of the form field with the sender's phone number.
FIELD_PHONE = "phone"

## @brief Name of the form field with the message text.
FIELD_MESSAGE = "message"

## @brief Names of all contact form fields, in display order.
CONTACT_FIELDS = (FIELD_NAME, FIELD_EMAIL, FIELD_PHONE, FIELD_MESSAGE)

## @brief Heading shown (and returned by /form-entry) after a message is sent.
MSG_SENT_TEXT = "Successfully sent your message"

## @brief Markup returned by the /form-entry route.
FORM_ENTRY_RESPONSE = f"<h1>{MSG_SENT_TEXT}</h1>"

## @brief Template names of the blog.
TEMPLATE_INDEX = "index.html"
TEMPLATE_ABOUT = "about.html"
TEMPLATE_POST = "post.html"
TEMPLATE_CONTACT = "contact.html"

## @brief File name of the bundled blog posts.
POSTS_FILE_NAME = "posts.json"

## @brief Environment variable names of the SMTP settings.
ENV_MAIL_HOST = "MAIL_HOST"
ENV_MAIL_PORT = "MAIL_PORT"
ENV_MAIL_USER = "MAIL_USER"
ENV_MAIL_PASSWORD = "MAIL_PASSWORD"
ENV_MAIL_RECIPIENT = "MAIL_RECIPIENT"
ENV_MAIL_USE_TLS = "MAIL_USE_TLS"

## @brief SMTP submission port used when MAIL_PORT is not set.
DEFAULT_MAIL_PORT = 587

## @brief Values of MAIL_USE_TLS that switch STARTTLS off (compared lower case).
MAIL_TLS_OFF_VALUES = ("false", "0")

## @brief Seconds to wait for the SMTP server before giving up.
SMTP_TIMEOUT_SECONDS = 10

## @brief Subject of the email sent for a contact form message.
MAIL_SUBJECT = "New Message from the blog contact form"

## @brief Labels of the lines in the email body.
MAIL_LABEL_NAME = "Name"
MAIL_LABEL_EMAIL = "Email"
MAIL_LABEL_PHONE = "Phone Number"
MAIL_LABEL_MESSAGE = "Message"

## @brief Header names of the email.
MAIL_HEADER_FROM = "From"
MAIL_HEADER_TO = "To"
MAIL_HEADER_REPLY_TO = "Reply-To"
MAIL_HEADER_SUBJECT = "Subject"

## @brief Message of the error raised when no SMTP settings exist.
MAIL_NOT_CONFIGURED_TEXT = "mail is not configured"

## @brief Text shown to the visitor when the email could not be sent.
MAIL_DELIVERY_FAILED_TEXT = "Your message could not be sent. Please try again later."

## @brief Text shown to the visitor when the form values are not acceptable.
CONTACT_INVALID_TEXT = "Please check your entries and try again."

## @brief Characters that must not appear in a header value.
LINE_BREAK_CHARACTERS = ("\r", "\n")

## @brief HTTP status codes of the contact route failures.
HTTP_BAD_REQUEST = 400
HTTP_BAD_GATEWAY = 502
