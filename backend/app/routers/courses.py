# backend/app/routers/courses.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..database.connection import get_db
from ..models import Course
from ..schemas import CourseCreate, CourseRead

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.post("/", response_model=CourseRead)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.name == course.name))
    existing_course = result.scalars().first()
    if existing_course:
        raise HTTPException(status_code=400, detail="Курс уже существует")
    new_course = Course(**course.dict())
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course

@router.get("/", response_model=list[CourseRead])
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course))
    courses = result.scalars().all()
    return courses

@router.get("/{course_id}", response_model=CourseRead)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Курс не найден")
    return course
