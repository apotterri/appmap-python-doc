import pytest
from app import app as _app


@pytest.fixture()
def app():
    _app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield _app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()
