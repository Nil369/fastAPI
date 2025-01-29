from fastapi import FastAPI

app = FastAPI()

# @app.get("/")

# +++++++++++++++ path params +++++++++++++++++
@app.get("/items/{item_id}")
async def read_items(item_id:int):
    return {"item_id":item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# ++++++++++ Enum class +++++++++++++++++
from enum import Enum

class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message":"Learning Deep Learning fr!"}

    if model_name =="lenet":
        return {"model_name":model_name,"message":"LeCNN for all images"}

    return {"model_name":model_name,"message":"Other remaining models"}