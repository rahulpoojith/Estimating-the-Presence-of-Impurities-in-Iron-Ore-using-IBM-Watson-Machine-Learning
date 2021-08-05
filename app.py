import requests
import json 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
API_KEY = "8oGQA18Ptfq-ow1-lN4DkZD5Hqe8NvBP_LHRbR_T4PJ8"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)
              
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return  render_template("about.html")
@app.route('/y_predict',methods=['POST'])
def y_predict():

    i = request.form["% Iron Feed"]
    s = request.form["Starch Flow"]
    a = request.form["Amina Flow"]
    opf = request.form["Ore Pulp Flow"]
    opp = request.form["Ore Pulp pH"]
    opd = request.form["Ore Pulp Density"]
    aaf = request.form["aaf_1456"]
    afl = request.form["afl_1456"]
    
    v = [[float(i),float(s),float(a),float(opf),float(opp),float(opd),float(aaf),float(afl)]]
    #[[49.75,2710.94,441.052,386.570,9.62129,1.65365,312.17025,438.69750]]
    
    
    payload_scoring = {"input_data": [{"field": ["% Iron Feed","Starch Flow","Amina Flow","Ore Pulp Flow","Ore Pulp Ph","Ore Pulp Density","aaf_1456","afl_1456"], "values": v }]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/839436af-a774-4531-b78b-6b3d9401953e/predictions?version=2021-08-03', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    #print("Scoring response")
    pred_ = response_scoring.json()
    
    pred = pred_['predictions'][0]['values'][0][0]
    print(pred)
    
    pred=str(pred)
    
    return render_template('index.html', prediction_text = pred)

    

if __name__ == "__main__":
    app.run(debug=True)



