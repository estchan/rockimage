import os
from typing import Any, Optional


def config(key: str, cast: Optional[Any] = None, default: Optional[Any] = None) -> Any:
    value = os.getenv(key, default)
    if cast:
        return cast(value)
    return value


ENVIRONMENT = config("ENVIRONMENT", default="local", cast=str)
ENABLE_API = config("ENABLE_API", default=ENVIRONMENT is "local", cast=bool)
DATABASE_URL = config("DATABASE_URL", default="postgresql://localhost/rockimage")
STORAGE_BUCKET = config("STORAGE_BUCKET", default="rockimage-storage")

DATASTORE = config('DATASTORE', default='sql')
