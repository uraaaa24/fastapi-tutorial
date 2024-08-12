from typing import Union

from fastapi import APIRouter, Body, FastAPI, Path, Query
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(
        default=None, title="The price must be greater than zero", gt=0
    )
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        ...,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@router.get("/items/{item_id}")
async def read_items_by_id(
    *,
    item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),
    q: str,
    size: float = Query(default=None, gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@router.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., embed=True),
):
    results = {"item_id": item_id, "item": item}
    return results
