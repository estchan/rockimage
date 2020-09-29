from abc import ABC, abstractmethod
from typing import Any

from google.cloud import storage

from rockimage import config


class Storage(ABC):
    @abstractmethod
    def write(self, path: str, stream: Any):
        pass


class GoogleCloudStorage(Storage):
    def __init__(self, bucket: str = config.STORAGE_BUCKET):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket)

    def write(self, path: str, stream: Any):
        blob = self.bucket.blob(path)
        blob.upload_from_file(stream)

storage = GoogleCloudStorage()
