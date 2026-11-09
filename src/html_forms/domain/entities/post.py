"""!
@file post.py
@brief The Post entity of the blog.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Post:
    """!
    @brief One blog post.
    @param id Unique number of the post.
    @param title Headline.
    @param subtitle Short line under the headline.
    @param body Paragraphs separated by a blank line.
    @param author Name of the author.
    @param date Publication date as shown to the reader.
    @param image Optional image file name.
    """

    id: int
    title: str
    subtitle: str
    body: str
    author: str
    date: str
    image: str | None = None
