"""!
@file test_posts.py
@brief Unit tests of the post use cases and the JSON post repository.
"""

import json
from pathlib import Path

import pytest

from html_forms.application.use_cases.get_post import get_post
from html_forms.application.use_cases.list_posts import list_posts
from html_forms.domain.entities.post import Post
from html_forms.domain.errors.post_not_found_error import PostNotFoundError
from html_forms.infrastructure.post_repositories.json_post_repository import (
    JsonPostRepository,
)


class FakePostRepository:
    """!@brief In-memory fake of the PostRepository port."""

    def __init__(self, posts: list[Post]) -> None:
        """!
        @brief Store the posts.
        @param posts Posts to serve.
        """
        self._posts = posts

    def all(self) -> list[Post]:
        """!
        @brief Return every post.
        @return The posts.
        """
        return list(self._posts)

    def by_id(self, post_id: int) -> Post | None:
        """!
        @brief Find one post.
        @param post_id Id of the post.
        @return The post or None.
        """
        return next((p for p in self._posts if p.id == post_id), None)


def _post(post_id: int) -> Post:
    """!
    @brief Build a post for tests.
    @param post_id Id of the post.
    @return A post.
    """
    return Post(post_id, "T", "S", "B", "A", "D")


def test_list_posts_returns_all_posts() -> None:
    """!@brief The use case returns what the repository holds."""
    repository = FakePostRepository([_post(1), _post(2)])
    assert [p.id for p in list_posts(repository)] == [1, 2]


def test_list_posts_returns_empty_when_no_posts() -> None:
    """!@brief An empty repository gives an empty list."""
    assert list_posts(FakePostRepository([])) == []


def test_get_post_returns_matching_post() -> None:
    """!@brief The post with the id is returned."""
    repository = FakePostRepository([_post(1), _post(2)])
    assert get_post(repository, 2).id == 2


def test_get_post_raises_when_missing() -> None:
    """!@brief An unknown id raises PostNotFoundError."""
    with pytest.raises(PostNotFoundError) as error:
        get_post(FakePostRepository([_post(1)]), 99)
    assert error.value.post_id == 99


def test_json_repository_loads_bundled_posts() -> None:
    """!@brief The bundled file holds three posts with unique ids."""
    posts = JsonPostRepository().all()
    assert len(posts) == 3
    assert len({p.id for p in posts}) == 3


def test_json_repository_by_id_finds_post() -> None:
    """!@brief A bundled post is found by id."""
    post = JsonPostRepository().by_id(1)
    assert post is not None
    assert post.title


def test_json_repository_by_id_returns_none_when_missing() -> None:
    """!@brief An unknown id gives None."""
    assert JsonPostRepository().by_id(999) is None


def test_json_repository_reads_custom_file(tmp_path: Path) -> None:
    """!@brief The repository reads the file it is given, image defaults to None."""
    data = [
        {
            "id": 7,
            "title": "T",
            "subtitle": "S",
            "body": "B",
            "author": "A",
            "date": "D",
        }
    ]
    path = tmp_path / "posts.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    posts = JsonPostRepository(path).all()
    assert posts == [Post(7, "T", "S", "B", "A", "D", None)]
