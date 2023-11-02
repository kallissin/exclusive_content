from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session
from sqlalchemy import create_engine
from configs import config
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, onupdate=datetime.utcnow)


engine = create_engine(config.DB_URI)
Session = scoped_session(sessionmaker(bind=engine))