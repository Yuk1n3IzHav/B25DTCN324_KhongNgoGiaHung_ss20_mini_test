from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.student import StudentCreate
from services.student import get_all_students, create_student

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("", status_code=status.HTTP_200_OK)
def get_students(request: Request, db: Session = Depends(get_db)):
    return get_all_students(request.url.path, db)


@router.post("", status_code=status.HTTP_201_CREATED)
def add_student(
    student: StudentCreate, request: Request, db: Session = Depends(get_db)
):
    return create_student(student, request.url.path, db)
