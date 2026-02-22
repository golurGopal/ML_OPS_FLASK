from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)


f= open('classifier.pkl', 'rb')
model = pickle.load(f)


@app.route('/', methods=['GET'])
def ping():
    return {"message":"hello world"}

@app.route('/predict', methods=['POST'])
def prediction():
    data=request.get_json()

    if data["gender"]=="Male":
        gender= 1
    else:
        gender= 0
    if data["married"]=="Yes":
        married= 1
    else:
        married= 0

    applicantincome=float(data["ApplicantIncome"])
    loanamount=float(data["LoanAmount"])
    credithistory=float(data["Credit_History"])

    features= pd.DataFrame([{
        'Gender': gender,
        'Married': married,
        'ApplicantIncome': applicantincome,
        'LoanAmount': loanamount,
        'Credit_History': credithistory
    }])
    print(features)
    prediction=model.predict(features)
    print("here1")
    return {"loan_approval_status": int(prediction[0])}