from fastapi import FastAPI

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
    """{BASE_URL}/items/foo will return JSON response: {"item_id":"foo"}"""
    return {"item_id": item_id}

@app.get("/int_items/{item_id}")
async def read_int_item(item_id: int):  # Note: data validation for `int`
    """Data validation performed based on python type hint.
    - {BASE_URL}/items/1 will return JSON response: {"item_id":1}
    - {BASE_URL}/items/foo will return JSON response with error.
    - {BASE_URL}/items/4.2 will return JSON response with error.
    """
    return {"item_id": item_id}

