# FastAPI Reference Examples

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

### Async links

[When to use async vs sync functions](https://fastapi.tiangolo.com/async/#in-a-hurry)
