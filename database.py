from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Data_URL = "mysql+pymysql://root:28062007hung@localhost:3306/student_management_db"
engine = create_engine(Data_URL, echo=True)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

