# FatSecret API Integration with FastAPI

This project demonstrates how to integrate the FatSecret API using FastAPI. It includes endpoints to search for foods, retrieve food details, list food categories, log food intake, and get daily nutritional summaries.

## Features

- **Search Foods:** Search for food items using keywords.
- **Get Food Details:** Retrieve detailed information about a specific food item.
- **List Food Categories:** Fetch all available food categories.
- **Log Food Intake:** Log food consumption for users (mock implementation).


## Tech Stack

- **FastAPI:** Web framework for building APIs.
- **httpx:** HTTP client for making API requests.
- **Pydantic:** Data validation and settings management.
- **Dotenv:** Load environment variables from a `.env` file.

## Environment Variables

Create a `.env` file in the project root and add the following variables:

```env
FATSECRET_CLIENT_ID=<your-client-id>
FATSECRET_CLIENT_SECRET=<your-client-secret>
FATSECRET_AUTH_URL=https://oauth.fatsecret.com/connect/token
FATSECRET_API_URL=https://platform.fatsecret.com/rest/server.api
```

## Endpoints

### 1. **Search Foods**
- **URL:** `/foods/search`
- **Method:** `POST`
- **Request Body:** 
  ```json
  { "search_expression": "apple" }
  ```
- **Description:** Search for food items.

### 2. **Get Food Details**
- **URL:** `/foods/details/{food_id}`
- **Method:** `GET`
- **Description:** Get detailed information about a specific food item.

### 3. **List Food Categories**
- **URL:** `/foods/categories`
- **Method:** `GET`
- **Description:** Fetch all available food categories.

### 4. **Log Food Intake**
- **URL:** `/foods/log`
- **Method:** `POST`
- **Request Body:** 
  ```json
  {
    "user_id": "user123",
    "food_id": "12345",
    "quantity": 2,
    "date": "2025-01-28"
  }
  ```
- **Description:** Log a food item for a user and date (mock implementation).


## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd 2_IntegratingFatSecrets_FastAPI
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\Activate.ps1`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   #or
   fastapi dev main.py
   #or 
   fastapi dev main.py --port <availabe-port>
   ```
2. Open your browser or API client (e.g., Postman) and visit:
   ```
   http://127.0.0.1:8000/docs
   ```
   The interactive Swagger documentation will allow you to test the endpoints.

## Future Improvements

- Implement database integration for food logging.
- Add user authentication and role-based access control.
- Enhance nutritional summary calculations with real data.
