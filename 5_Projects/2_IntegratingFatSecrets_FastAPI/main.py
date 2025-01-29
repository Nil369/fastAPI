import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import httpx

# Load environment variables
load_dotenv()

# FatSecret API credentials and URLs
CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")
AUTH_URL = os.getenv("FATSECRET_AUTH_URL")
API_URL = os.getenv("FATSECRET_API_URL")

app = FastAPI()

# Models for request bodies
class FoodSearchRequest(BaseModel):
    search_expression: str

class FoodLogRequest(BaseModel):
    user_id: str
    food_id: str
    quantity: int
    date: str

# In-memory storage for logged food (mock implementation)
food_logs = []

# Get OAuth token
async def get_oauth_token():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                AUTH_URL,
                data={
                    "grant_type": "client_credentials",
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            return response.json()["access_token"]
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"OAuth error: {str(e)}")

# Search foods endpoint
@app.post("/foods/search")
async def search_foods(request: FoodSearchRequest):
    token = await get_oauth_token()
    params = {
        "method": "foods.search",
        "search_expression": request.search_expression,
        "format": "json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                API_URL,
                params=params,
                headers={"Authorization": f"Bearer {token}"},
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"API error: {str(e)}")

# Get food details endpoint
@app.get("/foods/details/{food_id}")
async def get_food_details(food_id: str):
    token = await get_oauth_token()
    params = {
        "method": "food.get",
        "food_id": food_id,
        "format": "json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                API_URL,
                params=params,
                headers={"Authorization": f"Bearer {token}"},
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"API error: {str(e)}")

# List food categories endpoint
@app.get("/foods/categories")
async def list_food_categories():
    token = await get_oauth_token()
    params = {
        "method": "foods.get_categories",
        "format": "json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                API_URL,
                params=params,
                headers={"Authorization": f"Bearer {token}"},
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"API error: {str(e)}")

# Log food intake (mock implementation)
@app.post("/foods/log")
async def log_food(request: FoodLogRequest):
    food_logs.append(request.dict())
    return {"message": "Food logged successfully", "log": request.dict()}

