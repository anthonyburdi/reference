from fastapi import FastAPI

# app provides all functionality of FastAPI
app = FastAPI()

# Routes defined using decorators referencing the endpoint path
# e.g. this route is http://127.0.0.1:8000/ when serving locally
# aka {base URL}/
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
