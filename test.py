import pytest
import requests
from fastapi.testclient import TestClient

from api import app
client = TestClient(app)

def test_predict_accept():
    res = client.post("/predict/10")
    assert res.status_code == 200
    assert res.text == '"Acceptée"'
    
def test_predict_reject():
    res = client.post("/predict/11")
    assert res.status_code == 200
    assert res.text == '"Rejetée"'
