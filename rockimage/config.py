from typing import Any
import os

def config(key: str, cast: Optional[Any] = None, default: Optional[Any] = None) -> Any:
    value = os.getenv(key, default)
    if cast:
        return cast(value)
    return value

DATABASE_URL = config("DATABASE_URL")
