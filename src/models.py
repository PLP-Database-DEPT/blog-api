from sqlmodel import SQLModel, Field, Column
from sqlalchemy import String, DateTime
import uuid
from datetime import datetime

class Blog(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(String(36), primary_key=True, unique=True, nullable=False)
    )
    title: str
    content: str | None = "my first blog ..."
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False)
    )

    def __repr__(self) -> str:
        return f"{self.title}"
