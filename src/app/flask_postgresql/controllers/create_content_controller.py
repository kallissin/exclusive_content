from src.app.flask_postgresql.interfaces.flask_postggresql_controller_interface import FlaskPostgresqlControllerInterface
from src.interactor.dtos.create_content_dtos import CreateContentInputDto
from src.app.flask_postgresql.presenters.create_content_presenter import CreateContentPresenter
from typing import Dict
from src.infra.repositories.content_postgresql_repository import ContentPostgresqlRepository
from src.interactor.use_cases.create_content import CreateContentUseCase


class CreateContentController(FlaskPostgresqlControllerInterface):

    def __init__(self):
        self.input_dto: CreateContentInputDto

    
    def get_profession_info(self, json_input) -> None:
        if "category" in json_input:
            category = json_input["category"]
        
        try:
            category = json_input["category"]
            content = json_input["content"]
            title = json_input["title"]
        except KeyError as err:
            raise ValueError(f"Missing {err.args}")
        
        self.input_dto = CreateContentInputDto(category, title, content)

    
    def execute(self) -> Dict:
        repository = ContentPostgresqlRepository()
        presenter = CreateContentPresenter()
        use_case = CreateContentUseCase(presenter, repository)
        result = use_case.execute(self.input_dto)
        return result
