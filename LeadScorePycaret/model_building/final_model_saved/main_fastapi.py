           # 1. Library imports
import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load trained Pipeline
model = load_model('diamond-pipeline')

# Define predict function
@app.post("/predict/")
def predict(carat_weight, cut, color, clarity, polish, symmetry, report):
    data = pd.DataFrame([[carat_weight, cut, color, clarity, polish, symmetry, report]])
    data.columns = ['Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']

    predictions = predict_model(model, data=data) 
    return {'prediction': int(predictions['Label'][0])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
# 4. Run the API with uvicorn
# uvicorn main:app --reload
# 5. Open the API in your browser: http://localhost:8000/docs

'''
to run the endpoint in a app.py file, run the following function:


import requests

def get_predictions(carat_weight, cut, color, clarity, polish, symmetry, report):
    url = 'http://localhost:8000/predict?carat_weight={carat_weight}&cut={cut}&color={color}&clarity={clarity}&polish={polish}&symmetry={symmetry}&report={report}'\
    .format(carat_weight = carat_weight, cut = cut, color = color, clarity = clarity, polish = polish, symmetry = symmetry, report = report)
    
    x = requests.post(url)
    print(x.text)
    
get_predictions(1.01, 'Ideal', 'E', 'SI2', 'VG', 'VG', 'GIA')


--------------------------------------------------------------- 2nd method ---------------------------------------------------------------

Create a FASTAPI endpoint for the model

# Import necessary libraries
import pickle
from fastapi import FastAPI
import pandas as pd
from pycaret.regression import load_model

# Load the saved model
model = load_model('saved_model.pkl')

# Create a FastAPI object
app = FastAPI()

# Define the predict function for FastAPI
@app.post('/predict')
def predict(data: pd.DataFrame):
    predictions = model.predict(data)
    return {'predictions': list(predictions)}
    
use the following command to run the endpoint using request library:

import requests
import pandas as pd

# Load the dataset
data = pd.read_csv('unseen_data.csv')

# Define the endpoint URL
url = 'http://localhost:8000/predict'

# Send a POST request to the endpoint with the dataset as the request body
response = requests.post(url, json=data.to_dict(orient='records'))

# Get the predictions from the response
predictions = response.json()['predictions']

# Add the predicted label as a column
data['label_predicted'] = predictions

# Show the first 5 rows of the updated dataset
print(data.head(5))

'''