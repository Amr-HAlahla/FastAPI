from fastapi import APIRouter, Depends, status, Response
from .. import schemas
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blogs'])


@router.post('/{creator_id}', status_code=status.HTTP_201_CREATED)
# store the blogs into database
def create(creator_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
           # current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(db, creator_id, request)


@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db)):
    return blog.delete_blog(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(db, request, id)


# get the blog by a specific id
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    return blog.get_blog(db, id)
