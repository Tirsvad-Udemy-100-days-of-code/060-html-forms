"""!
@file json_post_repository.py
@brief Post repository that reads a bundled JSON file.
"""

import json
from pathlib import Path

from html_forms import constants
from html_forms.domain.entities.post import Post

## @brief Folder with the bundled data files.
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


class JsonPostRepository:
    """!@brief Implements the PostRepository port on a JSON file."""

    def __init__(self, path: Path | None = None) -> None:
        """!
        @brief Load the posts.
        @param path JSON file to read; the bundled file when None.
        """
        file_path = path if path is not None else DATA_DIR / constants.POSTS_FILE_NAME
        raw = json.loads(file_path.read_text(encoding="utf-8"))
        self._posts = [Post(**item) for item in raw]

    def all(self) -> list[Post]:
        """!
        @brief Return every post.
        @return The posts, in file order.
        """
        return list(self._posts)

    def by_id(self, post_id: int) -> Post | None:
        """!
        @brief Find one post.
        @param post_id Id of the post.
        @return The post, or None when it does not exist.
        """
        return next((post for post in self._posts if post.id == post_id), None)
