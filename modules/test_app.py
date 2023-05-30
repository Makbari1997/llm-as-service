from app import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_case_1():
    response = client.post("/intent_detection", json={"utterance": "Is Babar: King of the Elephants playing"})
    assert response.status_code == 200
    assert response.json() == {"intent":"SearchScreeningEvent"}

def test_case_2():
    response = client.post("/intent_detection", json={"utterance": "Open itunes and play Ben Burnley Ready To Die"})
    assert response.status_code == 200
    assert response.json() == {"intent": "PlayMusic"}

def test_case_3():
    response = client.post("/intent_detection", json={"utterance": "Rate The Guilty 0 of 6 points"})
    assert response.status_code == 200
    assert response.json() == {"intent": "RateBook"}

def test_case_4():
    response = client.post("/intent_detection", json={"utterance": "Please search for Switched"})
    assert response.status_code == 200
    assert response.json() == {"intent": "SearchCreativeWork"}

def test_case_5():
    response = client.post("/intent_detection", json={"utterance": "Tell me if it will be snowy 8 hours from now in Mount Airy VI"})
    assert response.status_code == 200
    assert response.json() == {"intent": "GetWeather"}