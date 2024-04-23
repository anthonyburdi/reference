# FastAPI Reference Examples

## Status

These examples are created for fastapi:

- v0.110.2
- Through Request Body in the Tutorial - User Guide: https://fastapi.tiangolo.com/tutorial/body/

## FastAPI

- [Docs](https://fastapi.tiangolo.com/) [pypi](https://pypi.org/project/fastapi/) [repo](https://github.com/tiangolo/fastapi)
- [Awesome FastAPI](https://github.com/mjhea0/awesome-fastapi) [Awesome FastAPI Projects](https://github.com/Kludex/awesome-fastapi-projects)

## Dev setup

### Run the live server

```bash
uvicorn main:app --reload
```

Where `app` is the instance of FastAPI() you created e.g. `app = FastAPI()` and `main` is the file defining your API e.g. `main.py`.

### API Docs

Using defaults, these are the links to api docs:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)
- [openapi.json](http://127.0.0.1:8000/openapi.json)

### HTTP Methods

Typical HTTP Methods:

- POST: to create data.
- GET: to read data.
- PUT: to update data.
- DELETE: to delete data.

### Async

[When to use async vs sync functions](https://fastapi.tiangolo.com/async/#in-a-hurry)

### Path params and Data Validation

Path params are specified via f-string syntax. Data validation performed based on the
type hint, including Enums. E.g.:

```python
@app.get("/int_items/{item_id}")
async def read_int_item(item_id: int):  # Note: data validation for `int`
    """Data validation performed based on python type hint.
    - {BASE_URL}/items/1 will return JSON response: {"item_id":1}
    - {BASE_URL}/items/foo will return JSON response with error.
    - {BASE_URL}/items/4.2 will return JSON response with error.
    """
    return {"item_id": item_id}
```
