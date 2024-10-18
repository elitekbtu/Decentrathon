# backend/shared/scripts/seed_database.py

import asyncio
from .add_courses import add_courses
from .add_modules import add_modules

async def seed():
    await add_courses()
    await add_modules()

if __name__ == "__main__":
    asyncio.run(seed())
