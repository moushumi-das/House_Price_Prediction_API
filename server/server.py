# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:57:39 2020

@author: moush
"""

from flask import Flask, request, jsonify
import util
app=Flask(__name__)

@app.route("/get_location") 
def get_location():
    response = jsonify({
        'locations': util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedroom = int(request.form['bedroom'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bedroom,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__== "__main__":
    print("starting python flask server for home price prediction....")
    util.load_saved_artifacts()
    app.run()

