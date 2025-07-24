import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_grade_submission(async_client: AsyncClient):
    response = await async_client.post("/grade", json={"answer": "This is a test answer"})
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert isinstance(data["score"], float)
    assert 0 <= data["score"] <= 1.0


async def test_grade_empty_answer(async_client: AsyncClient):
    response = await async_client.post("/grade", json={"answer": ""})
    assert response.status_code == 200
    data = response.json()
    assert data["score"] == 0.0


async def test_grade_validation(async_client: AsyncClient):
    # Test missing answer field
    response = await async_client.post("/grade", json={})
    assert response.status_code == 422

    # Test invalid JSON
    response = await async_client.post("/grade", content="invalid json")
    assert response.status_code == 422
