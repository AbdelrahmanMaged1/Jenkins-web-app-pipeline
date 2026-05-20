import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    """Homepage must respond with HTTP 200 OK"""
    response = client.get('/')

    assert response.status_code == 200


def test_home_contains_dashboard_title(client):
    """Page must contain the dashboard title text"""
    response = client.get('/')

    assert b'Data Pipeline' in response.data


def test_post_not_allowed(client):
    """Only GET is allowed on homepage"""
    response = client.post('/')

    assert response.status_code == 405