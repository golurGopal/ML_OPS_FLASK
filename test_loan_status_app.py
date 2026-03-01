import pytest
from loan_status import app
import json 



@pytest.fixture
def client():
    return app.test_client()



def test_ping(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "hello world"}

def test_prediction(client):
    payload = {
    "gender": "Male",
    "married": "Yes",
    "ApplicantIncome": 500000,
    "LoanAmount": 5000000,
    "Credit_History": 1
    }  

    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": 0}