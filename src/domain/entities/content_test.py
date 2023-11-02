from src.domain.entities.content import Content
from uuid import uuid4
from datetime import datetime


def test_content_creation_success(fixture_content):
    content = Content(
        content_id=fixture_content["content_id"],
        category=fixture_content["category"],
        title=fixture_content["title"],
        content=fixture_content["content"],
        created_at=fixture_content["created_at"],
        updated_at=fixture_content["updated_at"],
    )

    assert content.content == fixture_content["content"]
    assert content.category == fixture_content["category"]
    assert content.title == fixture_content["title"]
    assert content.created_at == fixture_content["created_at"]
    assert content.updated_at == fixture_content["updated_at"]


def test_content_from_dict(fixture_content):
    content = Content.from_dict(fixture_content)

    assert content.content == fixture_content["content"]
    assert content.category == fixture_content["category"]
    assert content.title == fixture_content["title"]
    assert content.created_at == fixture_content["created_at"]
    assert content.updated_at == fixture_content["updated_at"]


def test_content_to_dict(fixture_content):
    content = Content.from_dict(fixture_content)

    assert content.to_dict() == fixture_content
