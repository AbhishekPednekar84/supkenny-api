import uuid
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from database.db import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    name = Column(String(50))
    email = Column(String(50))
    message = Column(String(1000))
    date_created = Column(DateTime, index=True, default=datetime.now)

    def __repr__(self) -> str:
        return f"Message({self.id}, {self.name}, {self.email})"


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    email = Column(String(50), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Message({self.id}, {self.email})"
