import pytest
from unittest.mock import patch
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_health_page(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_get_quote(app):  # Here app is the fixture function you defined above.
    with app.test_client() as other_client:
        with patch('requests.get') as mock_get:
            class MockResponse:
                def __init__(self):
                    self.text = 'This is a quote'

            mock_get.return_value = MockResponse()
            
            response = other_client.get('/get_quote')

            assert response.status_code == 200
            assert b"This is a quote" in response.data




