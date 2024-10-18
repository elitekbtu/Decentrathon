# backend/app/main.py

from fastapi import FastAPI
from .routers import users_router, courses_router, modules_router, progress_router
from .database.connection import engine, Base
import uvicorn
from .utils.logger import logger

app = FastAPI(
    title="LMS Telegram Mini App Backend",
    description="Backend server for LMS Telegram Mini App",
    version="1.0.0"
)

# Подключение маршрутов
app.include_router(users_router)
app.include_router(courses_router)
app.include_router(modules_router)
app.include_router(progress_router)

@app.on_event("startup")
async def startup():
    # Создание всех таблиц
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database connected and tables created.")

@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
    logger.info("Database connection closed.")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
