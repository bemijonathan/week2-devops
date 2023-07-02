import pytest
from unittest.mock import patch
from app import app as flask_app
import requests


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_health_page(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

