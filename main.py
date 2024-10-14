from fastapi import FastAPI, Request
from pydantic import BaseModel
from addition import add
from multiplication import multiply

app = FastAPI()

# class RequestBody(BaseModel):
#     request_type: str
#     a: int
#     b: int

# @app.post("/calculate")
# async def calculate(request_body: RequestBody):
#     if request_body.request_type == "multiply":
#         result = multiply(request_body.a, request_body.b)
#     elif request_body.request_type == "add":
#         result = add(request_body.a, request_body.b)
#     else:
#         return {"error": "Invalid request_type"}
#     return {"output": result}

from fastapi import FastAPI
from addition import add
from multiplication import multiply

app = FastAPI()

@app.get("/calculate")
def calculate(request_type: str, a: int, b: int):
    if request_type == "multiply":
        result = multiply(a, b)
    elif request_type == "add":
        result = add(a, b)
    else:
        return {"error": "Invalid request_type"}
    return {"output": result}
