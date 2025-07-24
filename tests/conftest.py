import pytest
from httpx import AsyncClient

from tutor_stack_assessment.main import app


@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
