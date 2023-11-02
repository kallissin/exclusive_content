from src.infra.db_models.db_base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import UnicodeText, Unicode
from sqlalchemy_utils import ChoiceType
import uuid
from src.infra.db_models import CATEGORY


class ContentModel(Base):
    __tablename__ = "contents"

    content_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category: Mapped[str] = mapped_column(ChoiceType(CATEGORY), nullable=False)
    title: Mapped[str] = mapped_column(Unicode(length=128), nullable=False)
    content: Mapped[str] = mapped_column(UnicodeText, nullable=False)
