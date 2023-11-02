from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.create_content_dtos import CreateContentOutputDto


class CreateContentPresenterInterface(ABC):

    @abstractmethod
    def present(self, output_dto: CreateContentOutputDto) -> Dict:
        """_summary_

        Args:
            output_dto (CreateContentOutputDto): CreateContentOutputDto

        Returns:
            Dict: dict
        """