from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas


def create_blog(db: Session, creator_id: int, request: schemas.Blog):
    user = db.query(models.User).filter(models.User.user_id == creator_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {creator_id} isn't available in our database")

    new_blog = models.Blog(**request.dict(), user_id=creator_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db: Session):
    blogs = (db.query(models.Blog)).all()
    return blogs  # a list of blogs(dictionary)


def get_blog(db: Session, id: int):
    my_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not my_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id = {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id = {id} is not available "}
    return my_blog


def update_blog(db: Session, request: schemas.Blog, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id = {id} is not available")

    blog.update({models.Blog.title: request.title, models.Blog.body: request.body}, synchronize_session=False)
    # blog.update(request)
    db.commit()
    return 'Updated'


def delete_blog(db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id = {id} is not available")

    blog.delete(synchronize_session=False)
    db.commit()
    return status.HTTP_204_NO_CONTENT
