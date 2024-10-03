from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.testing.pickleable import User

from queries.database import Base
import datetime
import uuid


class UsersOrm(Base):
    __tablename__ = 'users'
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, nullable=False)
    video_file_link: Mapped[str]
    text_file_link: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), nullable=False)
