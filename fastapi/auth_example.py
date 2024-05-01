"""This module is an exploration of security features in FastAPI
Based on https://fastapi.tiangolo.com/tutorial/security/ for v0.110.3

To run this app, use `uvicorn auth_example:auth_example_app --reload`

It currently covers through:
https://fastapi.tiangolo.com/tutorial/security/first-steps/#the-password-flow
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

auth_example_app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@auth_example_app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
