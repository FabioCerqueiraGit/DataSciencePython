'''
create a model and deploy on fastapi:

1. import the necessary libraries
2. create a fastapi app
3. create a class for the data with pydantic
4. load the model
5. define the predict function
6. define the endpoint
7. run the endpoint in a app.py file, run the following function:
8. import requests
9. 


'''

# 1. Import necessary libraries
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model
import uvicorn

# 2. Create the app object

app = FastAPI()

# 3. load the dataset into a dataframe

input_df = pd.read_excel("C:/Users/marce/Desktop/Python/pythoncheatsheets/python_projects/Lead_scoring/archive/Lead_new.xlsx")


# 4. load the model

model = load_model("Final_Bagged_L_Regre_12Feb2023")

# 5. Define the predict function getting the features from the dataframe

@app.post('/predict')
async def predict(data: pd.DataFrame):
    predictions = predict_model(model, data=data)
    return {'predictions': list(predictions)}




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)





 