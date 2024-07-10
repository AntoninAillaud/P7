import pytest
import requests

from api import app

def test_predict_accept():
    res = requests.post("http://127.0.0.1:8000/predict/10")
    assert res.status_code == 200
    assert res.text == '"Acceptée"'
    
def test_predict_reject():
    res = requests.post("http://127.0.0.1:8000/predict/11")
    assert res.status_code == 200
    assert res.text == '"Rejetée"'