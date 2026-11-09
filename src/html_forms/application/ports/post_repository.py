"""!
@file post_repository.py
@brief Port: where the blog posts come from.
"""

from typing import Protocol

from html_forms.domain.entities.post import Post


class PostRepository(Protocol):
    """!@brief Read access to blog posts."""

    def all(self) -> list[Post]:
        """!
        @brief Return every post.
        @return The posts, in display order.
        """
        ...

    def by_id(self, post_id: int) -> Post | None:
        """!
        @brief Find one post.
        @param post_id Id of the post.
        @return The post, or None when it does not exist.
        """
        ...
