import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_weather_api_no_city(client):
    response = client.get('/weather')
    assert response.status_code == 400

def test_weather_api_invalid_city(client, monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 404
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)
    response = client.get('/weather?city=unknown')
    assert response.status_code == 404
