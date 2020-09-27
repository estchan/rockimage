from sqlalchemy import Column, String
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import UUID

from rockimage.db import Base


class Image(Base):

    __tablename__ = "images"

    uuid = Column(
        UUID(as_uuid=True),
        server_default=text("uuid_generate_v4()"),
        primary_key=True,
        index=True,
    )
    path = Column(String, nullable=False)
