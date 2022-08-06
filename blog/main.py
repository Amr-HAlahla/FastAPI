from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, login

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(user.router)
app.include_router(blog.router)
