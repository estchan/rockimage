from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

import sqlalchemy as sa

from rockimage import config, db, models


@dataclass
class ImageRecord:
    path: str
    uuid: str


class Repository(ABC):
    @abstractmethod
    def get_image(self, uuid: str) -> Optional[ImageRecord]:
        pass

    @abstractmethod
    def get_images() -> List[ImageRecord]:
        pass

    @abstractmethod
    def save_image(self, uuid: str, path: str) -> ImageRecord:
        pass


class SQLRepository(Repository):
    def get_image(self, uuid: str) -> Optional[ImageRecord]:
        result = db.session.query(models.Image).first()
        if not result:
            return None
        return ImageRecord(path=result.path, uuid=result.uuid)

    def get_images(self) -> Optional[ImageRecord]:
        results = db.session.query(models.Image).all()
        return [ImageRecord(path=result.path, uuid=result.uuid) for result in results]

    def save_image(self, uuid: str, path: str) -> ImageRecord:
        image = models.Image(uuid=uuid, path=path)
        db.session.add(image)
        db.session.commit()
        return ImageRecord(uuid=uuid, path=path)


repository = SQLRepository()
