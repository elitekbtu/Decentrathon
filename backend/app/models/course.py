# backend/app/models/course.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..database.connection import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    
    modules = relationship("Module", back_populates="course")
