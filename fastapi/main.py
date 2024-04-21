from fastapi import FastAPI

# app provides all functionality of FastAPI
app = FastAPI()

# Routes defined using decorators referencing the endpoint path
# e.g. this route is http://127.0.0.1:8000/ when serving locally
@app.get("/")
async def root():
    """This method `root` defines what code is run when requesting the `/` route."""
    return {"message": "Hello World"}
