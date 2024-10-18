# backend/tests/test_users.py

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.database.connection import get_db
from app.models import Base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL_TEST = os.getenv('DATABASE_URL_TEST')  # Создайте отдельную тестовую базу

engine_test = create_async_engine(DATABASE_URL_TEST, echo=True)
TestingSessionLocal = sessionmaker(
    bind=engine_test,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest.fixture(scope="module")
async def async_session():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="module")
async def client(async_session: AsyncSession):
    async def override_get_db():
        yield async_session

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    response = await client.post("/users/", json={
        "telegram_id": "123456789",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["telegram_id"] == "123456789"
    assert data["username"] == "testuser"
    assert data["first_name"] == "Test"
    assert data["last_name"] == "User"
    assert data["tokens"] == 0
