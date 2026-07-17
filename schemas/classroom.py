from pydantic import BaseModel


class ClassroomResponse(BaseModel):
    id: int
    class_code: str
    class_name: str

    class Config:
        from_attributes = True