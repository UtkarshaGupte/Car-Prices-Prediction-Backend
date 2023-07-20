****Backend Service in FastAPI and Python****

This repository contains a backend service developed in FastAPI and Python that provides car price predictions using an H2O model. The service receives car details as input through an API endpoint and returns the predicted car price.

**Getting Started**

Follow the steps below to set up the backend service and start making predictions.

**Prerequisites**
1. Python 3.7 or higher
2. H2O.ai Python library (h2o)
3. FastAPI library (fastapi)
4. pandas library

**Installation**
1. Clone the repository:
git clone https://github.com/<your-username>/car-price-prediction-backend.git

2. Install the required libraries using pip:
pip install fastapi h2o pandas

**Usage**
1. Start the FastAPI server:
uvicorn main:app --reload

The server will start running at http://127.0.0.1:8000.

**API Endpoint**
Endpoint: /car-price-prediction/
Method: POST
Request Payload

The endpoint expects a JSON payload containing car details in the following format:

json
{
  "mark": "string",
  "model": "string",
  "generation_name": "string",
  "year": "integer",
  "mileage": "float",
  "vol_engine": "float",
  "fuel": "string",
  "city": "string",
  "province": "string"
}

Response
The server will respond with a JSON containing the predicted car price:

json
{
  "predicted_price": "float"
}
Notes

Make sure to update the model_path variable with the correct path to your trained H2O model file.
Ensure that the frontend URL in the origins list is updated to allow Cross-Origin Resource Sharing (CORS) for your frontend application.
