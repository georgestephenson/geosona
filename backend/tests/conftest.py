"""
Pytest configuration and shared fixtures
"""

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI app
    """
    return TestClient(app)


@pytest.fixture
def async_client():
    """
    Create an async test client for the FastAPI app
    """
    from httpx import AsyncClient, ASGITransport

    async def _get_client():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as ac:
            yield ac

    return _get_client
