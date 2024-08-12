from typing import List, Set, Union

from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: Union[str, None] = Field(
        default=None,
        title="The description of the item",
        max_length=300,
        examples=["An amazing item"],
    )
    price: float = Field(
        default=None, title="The price must be greater than zero", gt=0, examples=[35.4]
    )
    tax: Union[float, None] = Field(default=None, examples=[3.2])
    tags: Set[str] = Field(default=set(), examples=[["rock", "metal", "bar"]])
    image: Union[List[Image], None] = Field(
        default=None,
        examples=[
            [
                {"url": "http://example.com/baz.jpg", "name": "The Foo"},
                {"url": "http://example.com/bar.jpg", "name": "The Baz"},
            ]
        ],
    )

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": {
    #             "name": "Foo",
    #             "description": "An amazing item",
    #             "price": 35.4,
    #             "tax": 3.2,
    #             "tags": ["rock", "metal", "bar"],
    #             "image": [
    #                 {"url": "http://example.com/baz.jpg", "name": "The Foo"},
    #                 {"url": "http://example.com/bar.jpg", "name": "The Baz"},
    #             ],
    #         }
    #     }
    # }


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
