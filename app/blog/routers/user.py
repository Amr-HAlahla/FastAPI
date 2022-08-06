from fastapi import APIRouter, Depends
from blog import schemas
from typing import List
from sqlalchemy.orm import Session
from blog.database import get_db
from blog.repository import user
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['Users'])


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return user.create_user(db, request)


@router.get('/', response_model=List[schemas.ShowUsers])
def all_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.get_all_users(db)


@router.get('/{id}', response_model=schemas.ShowUsers)
def get_user(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.get_user(db, id)
