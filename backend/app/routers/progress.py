# backend/app/routers/progress.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..database.connection import get_db
from ..models import Progress, User, Module, Course
from ..schemas import ProgressCreate, ProgressRead

router = APIRouter(
    prefix="/progress",
    tags=["progress"]
)

@router.post("/", response_model=ProgressRead)
async def create_progress(progress: ProgressCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем существование пользователя
    result = await db.execute(select(User).where(User.id == progress.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    # Проверяем существование курса
    result = await db.execute(select(Course).where(Course.id == progress.course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Курс не найден")
    
    # Проверяем существование модуля
    result = await db.execute(select(Module).where(Module.id == progress.module_id))
    module = result.scalars().first()
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    
    # Проверяем, существует ли уже прогресс
    result = await db.execute(
        select(Progress).where(
            Progress.user_id == progress.user_id,
            Progress.module_id == progress.module_id
        )
    )
    existing_progress = result.scalars().first()
    if existing_progress:
        raise HTTPException(status_code=400, detail="Прогресс уже существует")
    
    new_progress = Progress(**progress.dict())
    db.add(new_progress)
    await db.commit()
    await db.refresh(new_progress)
    return new_progress

@router.get("/{user_id}", response_model=list[ProgressRead])
async def get_user_progress(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Progress).where(Progress.user_id == user_id))
    progresses = result.scalars().all()
    return progresses

@router.put("/{progress_id}", response_model=ProgressRead)
async def update_progress(progress_id: int, progress: ProgressCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Progress).where(Progress.id == progress_id))
    existing_progress = result.scalars().first()
    if not existing_progress:
        raise HTTPException(status_code=404, detail="Прогресс не найден")
    
    existing_progress.completed = progress.completed
    await db.commit()
    await db.refresh(existing_progress)
    return existing_progress
