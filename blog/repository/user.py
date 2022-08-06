from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: schemas.User):
    hashed_pass = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There's no any users")
    return users


def get_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id = {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id = {id} is not available "}
    return user
