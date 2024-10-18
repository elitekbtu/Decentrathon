# backend/app/services/token_management.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import User

async def add_tokens(user_id: int, amount: int, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user:
        user.tokens += amount
        db.add(user)
        await db.commit()

async def deduct_tokens(user_id: int, amount: int, db: AsyncSession):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user and user.tokens >= amount:
        user.tokens -= amount
        db.add(user)
        await db.commit()
        return True
    return False
