"""!
@file app.py
@brief The Day 60 blog with a working contact form (Flask).

Run with: python -m html_forms.presentation.features.blog.app
"""

import logging

from flask import Flask, abort, render_template, request

from html_forms import constants
from html_forms.application.ports.post_repository import PostRepository
from html_forms.application.use_cases.get_post import get_post
from html_forms.application.use_cases.list_posts import list_posts
from html_forms.domain.errors.post_not_found_error import PostNotFoundError
from html_forms.infrastructure.post_repositories.json_post_repository import (
    JsonPostRepository,
)

logger = logging.getLogger(__name__)


def _log_submission() -> None:
    """!
    @brief Log a summary of the submitted form, never the values themselves.
    """
    present = [field for field in constants.CONTACT_FIELDS if field in request.form]
    message_length = len(request.form.get(constants.FIELD_MESSAGE, ""))
    logger.info(
        "Contact form received: fields=%s, message_length=%d", present, message_length
    )


class BlogViews:
    """!
    @brief The view functions of the blog, bound to one post repository.
    """

    def __init__(self, posts: PostRepository) -> None:
        """!
        @brief Create the views.
        @param posts Post source used by the views.
        """
        self._posts = posts

    def home(self) -> str:
        """!
        @brief Show the list of posts.
        @return The rendered home page.
        """
        return render_template(constants.TEMPLATE_INDEX, posts=list_posts(self._posts))

    def about(self) -> str:
        """!
        @brief Show the about page.
        @return The rendered about page.
        """
        return render_template(constants.TEMPLATE_ABOUT)

    def show_post(self, post_id: int) -> str:
        """!
        @brief Show one post.
        @param post_id Id of the post.
        @return The rendered post page; HTTP 404 when the post does not exist.
        """
        try:
            post = get_post(self._posts, post_id)
        except PostNotFoundError:
            abort(404)
        return render_template(constants.TEMPLATE_POST, post=post)

    def contact(self) -> str:
        """!
        @brief Show the contact form; on POST accept it and show the success heading.
        @return The rendered contact page.
        """
        if request.method == "POST":
            _log_submission()
            return render_template(constants.TEMPLATE_CONTACT, msg_sent=True)
        return render_template(constants.TEMPLATE_CONTACT, msg_sent=False)

    def form_entry(self) -> str:
        """!
        @brief First version of the form handler (lecture step L5/L6).
        @return The success heading as an HTML string.
        """
        _log_submission()
        return constants.FORM_ENTRY_RESPONSE


def create_app(repository: PostRepository | None = None) -> Flask:
    """!
    @brief Build the Flask app (composition root of the blog).
    @param repository Post source; the bundled JSON repository when None.
    @return The configured Flask application.
    """
    app = Flask(__name__, template_folder="templates", static_folder="static")
    views = BlogViews(repository if repository is not None else JsonPostRepository())

    app.add_url_rule(
        constants.ROUTE_HOME, endpoint="home", view_func=views.home, methods=["GET"]
    )
    app.add_url_rule(
        constants.ROUTE_ABOUT, endpoint="about", view_func=views.about, methods=["GET"]
    )
    app.add_url_rule(
        constants.ROUTE_POST,
        endpoint="show_post",
        view_func=views.show_post,
        methods=["GET"],
    )
    app.add_url_rule(
        constants.ROUTE_CONTACT,
        endpoint="contact",
        view_func=views.contact,
        methods=["GET", "POST"],
    )
    app.add_url_rule(
        constants.ROUTE_FORM_ENTRY,
        endpoint="form_entry",
        view_func=views.form_entry,
        methods=["POST"],
    )

    return app


def main() -> None:
    """!@brief Run the blog on the development server."""
    create_app().run(host=constants.DEFAULT_HOST, port=constants.BLOG_PORT)


if __name__ == "__main__":
    main()
