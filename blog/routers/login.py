from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, token
from ..database import get_db
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

# from datetime import timedelta
# from ..token import ACCESS_TOKEN_EXPIRE_MINUTES, timedelta, create_access_token

router = APIRouter(
    prefix='/login',
    tags=['Authentication'])


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="This User Not Available")

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Wrong Password")

    # generate a jwt token and return it.

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
