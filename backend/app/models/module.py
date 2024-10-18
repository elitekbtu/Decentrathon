# backend/app/models/module.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Module(Base):
    __tablename__ = 'modules'
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)  # Можно хранить текст, ссылки и т.д.
    
    course = relationship("Course", back_populates="modules")
    progress = relationship("Progress", back_populates="module")
