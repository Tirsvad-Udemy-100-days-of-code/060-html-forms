"""!
@file list_posts.py
@brief Use case: list all blog posts.
"""

from html_forms.application.ports.post_repository import PostRepository
from html_forms.domain.entities.post import Post


def list_posts(repository: PostRepository) -> list[Post]:
    """!
    @brief List all posts.
    @param repository Source of the posts.
    @return The posts, in display order.
    """
    return repository.all()
