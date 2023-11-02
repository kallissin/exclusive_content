from dataclasses import dataclass
from src.domain.value_objects import ContentId, CreatedAt, UpdatedAt


@dataclass
class Content:

    content_id: ContentId
    category: str
    title: str
    content: str
    created_at: CreatedAt
    updated_at: UpdatedAt


    @classmethod
    def from_dict(cls, data):
        """ Convert data from a dictionary
        """
        return cls(**data)
    

    def to_dict(self):
        """ Convert data into dictionary
        """
        return self.__dict__
