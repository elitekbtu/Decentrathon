# backend/app/schemas/__init__.py

from .user import UserCreate, UserRead
from .course import CourseCreate, CourseRead
from .module import ModuleCreate, ModuleRead
from .progress import ProgressCreate, ProgressRead

__all__ = [
    'UserCreate', 'UserRead',
    'CourseCreate', 'CourseRead',
    'ModuleCreate', 'ModuleRead',
    'ProgressCreate', 'ProgressRead'
]
