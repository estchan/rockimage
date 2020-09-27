from typing import Any, Optional
import os

def config(key: str, cast: Optional[Any] = None, default: Optional[Any] = None) -> Any:
    value = os.getenv(key, default)
    if cast:
        return cast(value)
    return value

ENABLE_API = config("ENABLE_API", default=False, cast=bool)
DATABASE_URL = config("DATABASE_URL", default="postgresql://localhost/rockimage")
