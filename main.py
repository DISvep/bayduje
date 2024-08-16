from fastapi import FastAPI
from typing import List, Any
from pydantic import BaseModel
import uvicorn


app = FastAPI()

users: List[Any] = []


class User(BaseModel):
    id: int
    username: str
    email: str


@app.get('/')
def index():
    return 'hello'


@app.post('/create_user', response_model=User)
def add_user(user: User):
    users.append(user)
    return user


@app.get('/users', response_model=List[User])
def get_all_users():
    return users


@app.get('/users/{user_id}', response_model=User)
def get_user(user_id: int):
    return users[user_id]


if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=1488, reload=True)
