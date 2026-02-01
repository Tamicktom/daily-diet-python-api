import pytest

from api import app as flask_app


@pytest.fixture
def app():
    """Provide the Flask application for pytest-flask."""
    flask_app.config["TESTING"] = True
    return flask_app
