from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    # id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
    # user_id: int


class ShowUsers(BaseModel):
    name: str
    email: str

    blogs: List[Blog]

    class Config:
        orm_mode = True


class ShowRelatedUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str

    user: ShowRelatedUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
