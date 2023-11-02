from dataclasses import dataclass
from src.domain.entities.content import Content


@dataclass
class CreateContentInputDto:
    category: str
    title: str
    content: str


@dataclass
class CreateContentOutputDto:
    content: Content
