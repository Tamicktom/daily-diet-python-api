"""Tests for the hello world route."""


def test_hello_returns_200(client):
    """GET /hello returns status 200."""
    response = client.get("/hello")
    assert response.status_code == 200


def test_hello_returns_json(client):
    """GET /hello returns JSON with message key."""
    response = client.get("/hello")
    assert response.content_type == "application/json"
    data = response.get_json()
    assert "message" in data


def test_hello_message_content(client):
    """GET /hello returns 'Hello, World!' message."""
    response = client.get("/hello")
    data = response.get_json()
    assert data["message"] == "Hello, World!"


def test_hello_method_not_allowed_for_post(client):
    """POST /hello returns 405 Method Not Allowed."""
    response = client.post("/hello")
    assert response.status_code == 405
