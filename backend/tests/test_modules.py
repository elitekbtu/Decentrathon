# backend/tests/test_modules.py

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_module(client: AsyncClient):
    # Предположим, что курс с ID 1 существует
    response = await client.post("/modules/", json={
        "course_id": 1,
        "title": "Введение в Python",
        "content": "Содержание модуля..."
    })
    assert response.status_code == 200
    data = response.json()
    assert data["course_id"] == 1
    assert data["title"] == "Введение в Python"
    assert data["content"] == "Содержание модуля..."
    assert "id" in data

@pytest.mark.asyncio
async def test_get_module(client: AsyncClient):
    # Предположим, что модуль с ID 1 существует
    response = await client.get("/modules/1")
    if response.status_code == 200:
        data = response.json()
        assert data["id"] == 1
        assert data["title"] == "Введение в Python"
    else:
        assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_modules_by_course(client: AsyncClient):
    response = await client.get("/modules/course/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
