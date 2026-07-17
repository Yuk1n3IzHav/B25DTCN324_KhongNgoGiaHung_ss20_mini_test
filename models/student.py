from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_code = Column(String(20), nullable=False)
    full_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    
    classroom = relationship("Classroom", back_populates="students")