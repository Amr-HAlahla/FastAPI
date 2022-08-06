from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('app/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):  # query parameters
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('app/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('app/blog/{id}')
def show(id: int):
    return {"data": id}


# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data': 'all unpublished blogs'}
# it will give an error if it comes after the above method bcz the parameter reserved as int type.

@app.get('app/blog/{id}/comments')
def comment():
    return {'data': {1, 2, 3}}


@app.get('app/blog/{id}/twitter')
def twitter(id: int):
    return {'data': 'Hello to my fans on twitter'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('app/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}, and a body with {blog.body}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
