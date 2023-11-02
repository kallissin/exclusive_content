from unittest.mock import patch
from src.domain.entities.content import Content


with patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.infra.db_models.content_db_models import ContentModel    
    from src.infra.repositories.content_postgresql_repository import ContentPostgresqlRepository


@patch("src.infra.repositories.content_postgresql_repository.uuid.uuid4")
@patch("src.infra.repositories.content_postgresql_repository.Session")
@patch("src.infra.repositories.content_postgresql_repository.ContentModel")
def test_content_postgresql_repository(mock_model, mock_session, mock_uuid, fixture_content):
    mock_uuid.return_value = fixture_content["content_id"]
    import ipdb; ipdb.set_trace()
    content_model = ContentModel(
        content_id=fixture_content["content_id"],
        category=fixture_content["category"],
        title=fixture_content["title"],
        content=fixture_content["content"],
        created_at=fixture_content["created_at"],
        updated_at=fixture_content["updated_at"],
    )

    mock_model.return_value = content_model
    repository = ContentPostgresqlRepository()
    
    result = repository.create(
        category=fixture_content["category"],
        title=fixture_content["title"],
        content=fixture_content["content"],
    )

    content = Content(
        content_id=fixture_content["content_id"],
        category=fixture_content["category"],
        title=fixture_content["title"],
        content=fixture_content["content"],
        created_at=fixture_content["created_at"],
        updated_at=fixture_content["updated_at"],
    )

    mock_session.add.assert_called_once_with(mock_model())
    mock_session.commit.assert_called_once_with()
    mock_session.refresh.assert_called_once_with(mock_model())

    assert result == content