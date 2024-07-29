# create a fast api app with a single endpoint of a pycaret model

# import libraries

from fastapi import FastAPI
from pycaret.classification import load_model, predict_model
import pandas as pd
import numpy as np 
import uvicorn
from pydantic import BaseModel
import pickle

import uvicorn

# create a fast api app

app = FastAPI()

# crete a class for the data with pydantic

class InputData(BaseModel):
    Prospect_ID: str
    Lead_Origin: str
    Lead_Source: str
    Do_Not_Email: str
    Do_Not_Call: str
    TotalVisits: int
    Total_Time_Spent_on_Website: int
    Page_Views_Per_Visit: float
    Last_Activity: str
    Specialization: str
    Search: str
    Get_updates_on_DM_Content: str
    City: str
    I_agree_to_pay_the_amount_through_cheque: str
    A_free_copy_of_Mastering_The_Interview: str
    Last_Notable_Activity: str

# load the model

model = pickle.load(open("Final_Bagged_L_Regre_12Feb2023.pkl", "rb"))

# Define the predict function
def predict(data: InputData):
    # Convert input data to a Pandas DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make predictions with the model
    predictions = model.predict(input_df)

    # Convert the predictions to a list of dictionaries
    predictions_list = predictions.tolist()
    output = [{"prediction": p} for p in predictions_list]

    return output

# Define the endpoint
@app.post("/predict")
async def predict_endpoint(data: InputData):
    return predict(data)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    

