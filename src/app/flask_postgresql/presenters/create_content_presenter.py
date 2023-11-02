from typing import Dict
from src.interactor.dtos.create_content_dtos import CreateContentOutputDto
from src.interactor.interfaces.presentes.create_content_presenter import CreateContentPresenterInterface


class CreateContentPresenter(CreateContentPresenterInterface):
    """ Class for the CreateContentPresenter
    """
    def present(self, output_dto: CreateContentOutputDto) -> Dict:
        """ Present the CreateContent
        :param output_dto: CreateContentOutputDto
        :return: Dict
        """
        return {
                    "content_id": output_dto.content.content_id,
                    "category": output_dto.content.category,
                    "title": output_dto.content.title,
                    "content": output_dto.content.content,
                    "created_at": output_dto.content.created_at,
                    "updated_at": output_dto.content.updated_at,
        }