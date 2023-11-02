from abc import ABC, abstractmethod
from src.domain.value_objects import ContentId
from src.domain.entities.content import Content


class ContentRepositoryInterface(ABC):

    @abstractmethod
    def get(self, content_id: ContentId) -> Content:
        """ Get s Content by id

        Args:
            content_id (ContentId): ContentId

        Returns:
            Content: Content
        """
    
    @abstractmethod
    def create(
        self, 
        category: str,
        title: str,
        content: str
    ) -> Content:
        """ Create a Content

        Args:
            category (Category): category
            title (str): title
            content (str): content

        Returns:
            Content: Content
        """