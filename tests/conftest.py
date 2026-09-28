import pytest
from fastapi.testclient import TestClient

from homebase.main import app


@pytest.fixture
def client():
    return TestClient(app)
