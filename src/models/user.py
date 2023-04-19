from typing import Union

from sqlmodel import Field

from texts.languages import LanguagesEnum

from .base import BaseModel


class User(BaseModel, table=True):
    id: str = Field(index=True, primary_key=True, nullable=False)
    username: Union[str, None]
    mention: Union[str, None]
    full_name: Union[str, None]

    language: str = Field(default=LanguagesEnum.ru)
