from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Classroom(Base):
    __tablename__ = "classrooms"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    class_code = Column(String(20), nullable=False)
    class_name = Column(String(50), nullable=False)
    
    students = relationship("Student", back_populates="classroom")