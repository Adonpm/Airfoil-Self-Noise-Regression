import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

#Loading pickle file containing the trained ML model
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route("/")
def home():
    #Go to home page
    return render_template('home.html')

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

#Creating a route for the web app
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]

    # Convert to 2D shape
    input_data = [data]

    # Make a prediction using the model
    prediction = model.predict(input_data)[0]
    print(prediction)
    
    # Return the prediction as a JSON response
    return render_template('home.html', prediction_text="Airfoil pressure is {}".format(prediction))
    
if __name__ == "__main__":
    app.run(debug=True)
