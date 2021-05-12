#!/usr/bin/env python3

"""
API to get predictions of price to a given apartment parameters
"""

from flask import Flask, request
import joblib

app = Flask(__name__)

@app.route('/prediction_apt/', methods=['GET'])
def prediction_apt():
    """
    http://localhost:5000/prediction_apt/?area=80&bedrooms=1&bathrooms=1&garages=1
    """
    model = joblib.load('data/rf_vr_model.pkl')
    area = request.args.get('area')
    bedrooms = request.args.get('bedrooms')
    bathrooms = request.args.get('bathrooms')
    garages = request.args.get('garages')
    prediction = model.predict([[area, bedrooms, bathrooms, garages]])
    res = prediction[0].astype(int).astype(str)

    return res, 200


if __name__ == '__main__':   
    app.run(debug=True)
