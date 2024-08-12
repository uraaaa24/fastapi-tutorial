from typing import List, Set, Union

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(
        default=None, title="The price must be greater than zero", gt=0
    )
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
