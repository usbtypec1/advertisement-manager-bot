import datetime
from typing import Annotated

from pydantic import BaseModel, Field

__all__ = ("User",)


class User(BaseModel):
    id: int
    full_name: Annotated[str, Field(max_length=64)]
    username: Annotated[str | None, Field(max_length=64)]
    created_at: datetime.datetime
