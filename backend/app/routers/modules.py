# backend/app/routers/modules.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..database.connection import get_db
from ..models import Module, Course
from ..schemas import ModuleCreate, ModuleRead

router = APIRouter(
    prefix="/modules",
    tags=["modules"]
)

@router.post("/", response_model=ModuleRead)
async def create_module(module: ModuleCreate, db: AsyncSession = Depends(get_db)):
    # Проверяем существование курса
    result = await db.execute(select(Course).where(Course.id == module.course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Курс не найден")
    new_module = Module(**module.dict())
    db.add(new_module)
    await db.commit()
    await db.refresh(new_module)
    return new_module

@router.get("/{module_id}", response_model=ModuleRead)
async def get_module(module_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Module).where(Module.id == module_id))
    module = result.scalars().first()
    if not module:
        raise HTTPException(status_code=404, detail="Модуль не найден")
    return module

@router.get("/course/{course_id}", response_model=list[ModuleRead])
async def get_modules_by_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Module).where(Module.course_id == course_id))
    modules = result.scalars().all()
    return modules
