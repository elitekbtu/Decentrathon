# backend/tests/test_courses.py

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_course(client: AsyncClient):
    response = await client.post("/courses/", json={
        "name": "Основы Python",
        "description": "Изучите базовые концепции программирования на Python."
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Основы Python"
    assert data["description"] == "Изучите базовые концепции программирования на Python."
    assert "id" in data

@pytest.mark.asyncio
async def test_get_courses(client: AsyncClient):
    response = await client.get("/courses/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

@pytest.mark.asyncio
async def test_get_course(client: AsyncClient):
    # Предположим, что курс с ID 1 существует
    response = await client.get("/courses/1")
    if response.status_code == 200:
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Основы Python"
    else:
        assert response.status_code == 404
