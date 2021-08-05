import requests
import json 
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "8oGQA18Ptfq-ow1-lN4DkZD5Hqe8NvBP_LHRbR_T4PJ8"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ["% Iron Feed","Starch Flow","Amina Flow","Ore Pulp Flow","Ore Pulp Ph","Ore Pulp Density","aaf_1456","afl_1456"], "values": [[49.75,2710.94,441.052,386.570,9.62129,1.65365,312.17025,438.69750]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/839436af-a774-4531-b78b-6b3d9401953e/predictions?version=2021-08-03', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
