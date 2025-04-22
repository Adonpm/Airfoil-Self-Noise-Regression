import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, app, jsonify

app = Flask('__name__')

#Loading pickle file containing the trained ML model
model = pickle.load(open('models/model.pkl', 'rb'))

#Creating an api
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)

    # Convert the input data to a list of values
    input_data = list(data.values())
    
    # Convert the input data to a 2D Array
    input_data = [list(data.values())]

    # Make a prediction using the model
    prediction = model.predict(input_data)[0]
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})
    
if __name__ == "__main__":
    app.run(debug=True)
