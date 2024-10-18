# backend/shared/scripts/add_modules.py

import asyncio
from app.database.connection import engine, AsyncSessionLocal
from app.models import Base, Module, Course

async def add_modules():
    async with AsyncSessionLocal() as session:
        # Получаем курсы
        result = await session.execute(select(Course))
        courses = result.scalars().all()
        
        modules = []
        for course in courses:
            if course.name == "Английский язык":
                modules.extend([
                    Module(course_id=course.id, title="Основы грамматики", content="Изучение основ грамматики английского языка."),
                    Module(course_id=course.id, title="Словарный запас", content="Расширение словарного запаса.")
                ])
            elif course.name == "Основы Python":
                modules.extend([
                    Module(course_id=course.id, title="Введение в Python", content="Содержание модуля..."),
                    Module(course_id=course.id, title="Переменные и Типы данных", content="Содержание модуля...")
                ])
            elif course.name == "Казахстанская история":
                modules.extend([
                    Module(course_id=course.id, title="Древняя история", content="Содержание модуля..."),
                    Module(course_id=course.id, title="Современная история", content="Содержание модуля...")
                ])
        
        session.add_all(modules)
        await session.commit()
        print("Модули добавлены.")

if __name__ == "__main__":
    asyncio.run(add_modules())
