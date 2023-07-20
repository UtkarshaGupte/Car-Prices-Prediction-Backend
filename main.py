import h2o
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",  # Update with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the H2O model
h2o.init()
model_path = 'GBM_model_python_1689459252964_4'
print(model_path)
model = h2o.load_model(model_path)

class Car(BaseModel):
    mark: str
    model: str
    generation_name: str
    year: int
    mileage: float
    vol_engine: float
    fuel: str
    city: str
    province: str

@app.post("/car-price-prediction/")
async def predict_car_price(car: Car):
    # Create a DataFrame from the car details
    data = pd.DataFrame(car.dict(), index=[0])

    # Convert the DataFrame to an H2O Frame
    h2o_data = h2o.H2OFrame(data)

    # Perform the car price prediction using the loaded model
    predictions = model.predict(h2o_data)

    # Get the predicted price
    predicted_price = predictions[0, 0]

    # Return the predicted price as a JSON response
    return {"predicted_price": predicted_price}