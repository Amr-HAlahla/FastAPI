from fastapi import APIRouter, Depends
from .. import schemas
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user
from ..oauth2 import get_current_user
from fastapi import HTTPException, status

router = APIRouter(
    prefix='/user',
    tags=['Users'])


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db, request)


@router.get('/', response_model=List[schemas.ShowUsers])
def all_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)


@router.get('/{id}', response_model=schemas.ShowUsers)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(db, id)


@router.delete('/{id}')
def delete_user(id, db: Session = Depends(get_db)):
    return user.delete_user(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_user(id, request: schemas.UpdateUser, db: Session = Depends(get_db)):
    return user.update_user(id, db, request)
