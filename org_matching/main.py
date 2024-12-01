# from fastapi import FastAPI
# from fastdash import FastDash
# import joblib
# import numpy as np

# # Load your pre-trained model
# model = joblib.load('your_model.pkl')

# app = FastAPI()
# dash_app = FastDash(app)

# @app.post("/predict")
# def predict(input_data: dict):
#     # Convert input to numpy array
#     features = np.array(input_data['features']).reshape(1, -1)
    
#     # Make prediction
#     prediction = model.predict(features)
    
#     return {"prediction": prediction.tolist()}