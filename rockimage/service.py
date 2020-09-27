from dataclasses import asdict

from rockimage.exceptions import NotFound
from rockimage.repository import repository


def get_image(uuid: str) -> dict:
    image = repository.get_image(uuid)
    if not image:
        raise NotFound()
    return asdict(image)


def list_images() -> [dict]:
    images = repository.get_images()
    return [asdict(image) for image in images]
