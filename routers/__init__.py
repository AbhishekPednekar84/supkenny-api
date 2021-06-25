from fastapi import APIRouter

from database.db import session_local

router = APIRouter()


# Dependency
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
