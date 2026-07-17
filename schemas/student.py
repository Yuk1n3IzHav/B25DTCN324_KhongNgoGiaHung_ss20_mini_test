from pydantic import BaseModel, Field

from schemas.classroom import ClassroomResponse


class StudentCreate(BaseModel):
    student_code: str = Field(..., min_length=3, max_length=20)
    full_name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., min_length=2, max_length=50)
    class_id: int = Field(..., ge=1)


class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: str
    classroom: ClassroomResponse

    class Config:
        from_attributes = True