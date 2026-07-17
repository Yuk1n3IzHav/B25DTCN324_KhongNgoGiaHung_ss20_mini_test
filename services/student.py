from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
from models import Student, Classroom
from schemas import StudentCreate


def response(statusCode, message, data, error, path):
    return {
        "statusCode": statusCode,
        "message": message,
        "data": data,
        "error": error,
        "path": path,
    }


def get_all_students(path: str, db: Session):
    students = db.query(Student).options(joinedload(Classroom)).all()

    if students is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không có sinh viên trong hệ thống",
        )

    return response(200, "Lấy danh sách sinh viên thành công!", students, "null", path)


def create_student(student: StudentCreate, path: str, db: Session):
    classroom = db.query(Classroom).filter(Classroom.id == student.class_id).first()

    if classroom is None:
        raise HTTPException(
            status_code=404,
            detail={
                "Không tìm thấy lớp học!",
            },
        )

    existed_student = (
        db.query(Student).filter(Student.student_code == student.student_code).first()
    )

    if existed_student:
        raise HTTPException(status_code=400, detail={"Mã sinh viên đã tồn tại!"})

    new_student = StudentCreate()
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return response(201, "Thêm mới sinh viên thành công", new_student, "null", path)
