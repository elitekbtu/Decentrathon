# backend/shared/scripts/add_courses.py

import asyncio
from app.database.connection import engine, AsyncSessionLocal
from app.models import Base, Course

async def add_courses():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncSessionLocal() as session:
        courses = [
            Course(name="Английский язык", description="Изучение английского языка."),
            Course(name="Основы Python", description="Базовые концепции программирования на Python."),
            Course(name="Казахстанская история", description="Изучение истории Казахстана.")
        ]
        session.add_all(courses)
        await session.commit()
        print("Курсы добавлены.")

if __name__ == "__main__":
    asyncio.run(add_courses())
