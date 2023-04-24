from typing import Union

from sqlmodel import Field

from .base import BaseModel


class User(BaseModel, table=True):
    id: str = Field(index=True, primary_key=True, nullable=False)
    username: Union[str, None]
    mention: Union[str, None]
    full_name: Union[str, None]

    language: Union[str, None]

    @property
    def verbose_name(self):
        return self.full_name or self.username or self.mention
