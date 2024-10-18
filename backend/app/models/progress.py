# backend/app/models/progress.py

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Progress(Base):
    __tablename__ = 'progress'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    module_id = Column(Integer, ForeignKey('modules.id'), nullable=False)
    completed = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="progress")
    module = relationship("Module", back_populates="progress")
