"""
Tests for main API endpoints
"""

import pytest
from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """Test root endpoint returns correct response"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to Geosona API"
    assert data["status"] == "running"
    assert data["version"] == "0.1.0"


def test_health_check(client: TestClient):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_hello_world(client: TestClient):
    """Test hello world endpoint"""
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}


@pytest.mark.asyncio
async def test_root_async(async_client):
    """Test root endpoint with async client"""
    async for ac in async_client():
        response = await ac.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["status"] == "running"
