from abc import ABC, abstractmethod
from dataclasses import dataclass

import sqlalchemy as sa

from rockimage import config, db, models


@dataclass
class ImageRecord:
    path: str
    uuid: str


class Repository(ABC):
    @abstractmethod
    def get_image(uuid: str) -> Optional[ImageRecord]:
        pass

    @abstractmethod
    def get_images() -> List[Image]:
        pass


class SQLRepository(Repository):
    def get_image(uuid: str) -> Optional[ImageRecord]:
        result = db.session.query(Image).first()
        if not result:
            return None
        return ImageRecord(path=result.path, uuid=result.uuid)

    def get_images() -> Optional[ImageRecord]:
        result = db.session.query(Image).all()
        if not result:
            return None
        return ImageRecord(path=result.path, uuid=result.uuid)

repository = SQLRepository()
