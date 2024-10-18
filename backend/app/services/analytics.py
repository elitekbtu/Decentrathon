# backend/app/services/analytics.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Progress, User, Module

async def get_user_progress(user_id: int, db: AsyncSession):
    result = await db.execute(
        select(Progress).where(Progress.user_id == user_id)
    )
    progresses = result.scalars().all()
    progress_details = []
    for progress in progresses:
        module = await db.execute(
            select(Module).where(Module.id == progress.module_id)
        )
        module = module.scalars().first()
        progress_details.append({
            "module_title": module.title,
            "completed": progress.completed
        })
    return progress_details

async def get_leaderboard(db: AsyncSession, limit: int = 10):
    result = await db.execute(
        select(User).order_by(User.tokens.desc()).limit(limit)
    )
    users = result.scalars().all()
    leaderboard = [{"username": user.username or user.first_name, "tokens": user.tokens} for user in users]
    return leaderboard
