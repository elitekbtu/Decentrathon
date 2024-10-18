# backend/app/routers/__init__.py

from .users import router as users_router
from .courses import router as courses_router
from .modules import router as modules_router
from .progress import router as progress_router

__all__ = ['users_router', 'courses_router', 'modules_router', 'progress_router']
