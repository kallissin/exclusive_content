from src.interactor.dtos.create_content_dtos import CreateContentInputDto, CreateContentOutputDto
from src.interactor.interfaces.presentes.create_content_presenter import CreateContentPresenterInterface
from src.interactor.interfaces.repositories.content_repository import ContentRepositoryInterface
from src.interactor.use_cases.create_content import CreateContentUseCase
from src.domain.entities.content import Content
from unittest.mock import patch


@patch("src.interactor.use_cases.create_content.CreateContentPresenterInterface")
@patch("src.interactor.use_cases.create_content.ContentRepositoryInterface")
def test_create_content(mock_repository, mock_presenter, fixture_content):
    content = Content(
        content_id=fixture_content["content_id"],
        category=fixture_content["category"],
        title=fixture_content["title"],
        content=fixture_content["content"],
        created_at=fixture_content["created_at"],
        updated_at=fixture_content["updated_at"],
    )

    mock_repository.create.return_value = content
    mock_presenter.present.return_value = "Test output"

    use_case = CreateContentUseCase(
        presenter=mock_presenter,
        repository=mock_repository    
    )

    create_content_input_dto = CreateContentInputDto(
        category="PYTHON",
        title="instalando Python",
        content="""pip install python"""
    )

    result = use_case.execute(input_dto=create_content_input_dto)
    mock_repository.create.assert_called_once()
    output_dto = CreateContentOutputDto(content)
    mock_presenter.present.assert_called_once_with(output_dto)
    assert result == "Test output"

