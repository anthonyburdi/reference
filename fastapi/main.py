"""This module shows examples of:
- Setting up GET routes using path & query params
- Using validation including using a pydantic model
- Sending a request body via POST route

It covers the following sections of the FastAPI tutorial (https://fastapi.tiangolo.com/tutorial/body/):
- First Steps
- Path Parameters
- Query Parameters
- Request Body
"""

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from decimal import Decimal

# app provides all functionality of FastAPI
app = FastAPI()


# Routes defined using decorators referencing the endpoint path
# e.g. this route is http://127.0.0.1:8000/ when serving locally
# using defaults aka {BASE_URL}/
@app.get("/")
async def root():
    """This method `root` defines what code is run when requesting the `/` route.

    It is defined as an async function since it does not communicate with any other
    services e.g. db and can be processed async. See also
    https://fastapi.tiangolo.com/async/#in-a-hurry
    """
    # Can return dict, list, str, int or other singular values or pydantic or ORM models
    # which will be serialized to JSON.
    return {"message": "Hello World"}


# Pass parameters with the same syntax as python format strings
@app.get("/items/{item_id}")
async def read_item(item_id):  # Note: no data validation since item_id is of type Any
    """http://127.0.0.1:8000/items/foo will return JSON response: {"item_id":"foo"}"""
    return {"item_id": item_id}


@app.get("/int_items/{item_id}")
async def read_int_item(item_id: int):  # Note: data validation for `int`
    """Data validation performed based on python type hint.
    - http://127.0.0.1:8000/items/1 will return JSON response: {"item_id":1}
    - http://127.0.0.1:8000/items/foo will return JSON response with error.
    - http://127.0.0.1:8000/items/4.2 will return JSON response with error.
    """
    return {"item_id": item_id}


class MyEnum(str, Enum):
    val1 = "val1"
    val2 = "val2"


@app.get("/enum/{enum}")
async def read_enum(enum: MyEnum):
    """Validates that path param can only be one of the enum values in MyEnum.

    E.g. only http://127.0.0.1:8000/enum/val1 or http://127.0.0.1:8000/enum/val2 are acceptable, other
    values return an error response http://127.0.0.1:8000/enum/this_will_error.
    """
    return {"enum": enum}


@app.get("/filepath/{file_path:path}")
async def read_file(file_path: str):
    """Use `:path` after the parameter to take an actual filepath.
    - http://127.0.0.1:8000/filepath/home/johndoe/myfile.txt -> {"file_path":"home/johndoe/myfile.txt"}
    Or with leading slash:
    - http://127.0.0.1:8000/filepath//home/johndoe/myfile.txt -> {"file_path":"/home/johndoe/myfile.txt"}
    """
    return {"file_path": file_path}


@app.get("/query_params/")
async def query_params(
    required: str, optional: str | None = None, default: int = 0, boolean: bool = False
):
    """Query params are params in the function but not the path in the decorator.
    - http://127.0.0.1:8000/query_params/?required=hi&boolean=no ->
    {"required":"hi","optional":null,"default":0,"boolean":false}
    - http://127.0.0.1:8000/query_params/?required=hi&optional=hola&boolean=True ->
    {"required":"hi","optional":"hola","default":0,"boolean":true}
    """
    return {
        "required": required,
        "optional": optional,
        "default": default,
        "boolean": boolean,
    }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    tax_pct: Decimal | None = None


@app.post("/items/{item_id}")
async def create_item(
    item_id: int, item: Item, optional_query_param: str | None = None
):
    """Reads request body as JSON, convert to Item type & validate data.
    Can be combined with path and/or query params.
    https://fastapi.tiangolo.com/tutorial/body/#request-body-path-query-parameters
    """
    with_tax = item.price * (1 + item.tax_pct)
    print(
        f"Item price: {item.price}, with tax: {with_tax}. Query param: {optional_query_param}"
    )
    return {
        "item_id": item_id,
        "price_with_tax": with_tax,
        "optional_query_param": optional_query_param,
        **item.model_dump(),
    }
