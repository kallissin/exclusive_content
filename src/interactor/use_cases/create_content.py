from typing import Dict
from src.interactor.dtos.create_content_dtos import CreateContentInputDto, CreateContentOutputDto
from src.interactor.interfaces.presentes.create_content_presenter import CreateContentPresenterInterface
from src.interactor.interfaces.repositories.content_repository import ContentRepositoryInterface


class CreateContentUseCase():
    def __init__(
            self,
            presenter: CreateContentPresenterInterface,
            repository: ContentRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

    
    def execute(
            self,
            input_dto: CreateContentInputDto
    ) -> Dict:
        content = self.repository.create(
            category=input_dto.category,
            title=input_dto.title,
            content=input_dto.content
        )
        output_dto = CreateContentOutputDto(content)
        return self.presenter.present(output_dto)