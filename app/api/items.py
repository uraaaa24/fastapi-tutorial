from datetime import datetime, time, timedelta
from typing import Any, Dict, List, Union
from uuid import UUID

from fastapi import APIRouter, Body, Cookie, Header, Path, Query
from schema.items import CarItem, Image, Item, Offer, PlaneItem

router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

dummy_items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@router.get("/items/", response_model=List[Item])
async def read_items(
    x_token: Union[List[str], None] = Header(default=None),
) -> Any:
    return {"X-Token values": x_token}


# @router.get("/items/")
# async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
# return {"ads_id": ads_id}


@router.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_items_by_id(item_id: str):
    return dummy_items[item_id]


@router.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return dummy_items[item_id]


@router.get(
    "/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"]
)
async def read_item_public_data(item_id: str):
    return dummy_items[item_id]


@router.get("keyword-weight", response_model=Dict[str, float])
async def read_keyword_weights():
    return {
        "foo": 2.3,
        "bar": 3.4,
    }


@router.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@router.post("/offers")
async def create_offer(offer: Offer):
    return offer


@router.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@router.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


@router.put("/items/{item_id}")
async def read_items_by_id(
    item_id: UUID,
    start_datetime: datetime = Body(...),
    end_datetime: datetime = Body(...),
    process_after: timedelta = Body(...),
    repeat_at: Union[time, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }


# @router.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         ...,
#         example={
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2,
#             "tags": ["rock", "metal", "bar"],
#             "image": [
#                 {"url": "http://example.com/baz.jpg", "name": "The Foo"},
#                 {"url": "http://example.com/bar.jpg", "name": "The Baz"},
#             ],
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
