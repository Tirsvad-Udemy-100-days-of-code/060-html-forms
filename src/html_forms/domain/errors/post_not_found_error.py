"""!
@file post_not_found_error.py
@brief Error raised when a post id does not exist.
"""


class PostNotFoundError(Exception):
    """!@brief No post has the requested id."""

    def __init__(self, post_id: int) -> None:
        """!
        @brief Build the error for one id.
        @param post_id The id that was not found.
        """
        super().__init__(f"Post {post_id} not found")
        self.post_id = post_id
