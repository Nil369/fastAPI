from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION
import uvicorn

app = FastAPI(
    title="Insurance Premium Prediction API",
    description="API to predict insurance premium based on user inputs",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Prediction",
            "description": "Operations related to insurance premium prediction."
        }
    ]
)

# human readable       
@app.get('/')
def home():
    return {
        'success': True,
        'message':'Insurance Premium Prediction API'
    }


# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'App is healthy! 🎉',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post('/predict', response_model=PredictionResponse, tags=["Prediction"])
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        host="localhost",
        port=8000,
        reload=True
    )