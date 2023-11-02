from src.interactor.interfaces.repositories.content_repository import ContentRepositoryInterface
from src.infra.db_models.db_base import Session
from src.infra.db_models.content_db_models import ContentModel
from typing import Optional
from src.domain.entities.content import Content
import uuid
from src.domain.value_objects import ContentId


class ContentPostgresqlRepository(ContentRepositoryInterface):
    def __init__(self) -> None:
        self.__session = Session

    
    def __db_to_entity(
            self, db_row: ContentModel
    ) -> Optional[Content]:
        return Content(
            content_id=db_row.content_id,
            category=db_row.category,
            title=db_row.title,
            content=db_row.content
        )
    
    def create(self, category: str, title: str, content: str) -> Optional[Content]:
        content_id = uuid.uuid4()
        content_db_model = ContentModel(
            content_id=content_id,
            category=category,
            title=title,
            content=content
        )

        self.__session.add(content_db_model)
        self.__session.commit()
        self.__session.refresh(content_db_model)

        if content_db_model is not None:
            return self.__db_to_entity(content_db_model)
        
    def get(self, content_id: ContentId) -> Optional[Content]:
        result = self.__session.query(ContentModel).get(content_id)

        if result is not None:
            return self.__db_to_entity(result)

        return None
