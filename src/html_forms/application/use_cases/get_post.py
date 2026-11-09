"""!
@file get_post.py
@brief Use case: get one blog post.
"""

from html_forms.application.ports.post_repository import PostRepository
from html_forms.domain.entities.post import Post
from html_forms.domain.errors.post_not_found_error import PostNotFoundError


def get_post(repository: PostRepository, post_id: int) -> Post:
    """!
    @brief Get one post.
    @param repository Source of the posts.
    @param post_id Id of the wanted post.
    @return The post.
    @throws PostNotFoundError when no post has the id.
    """
    post = repository.by_id(post_id)
    if post is None:
        raise PostNotFoundError(post_id)
    return post
