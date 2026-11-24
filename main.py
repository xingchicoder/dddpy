"""Bootstrap the FastAPI application and configure infrastructure."""

import logging
from contextlib import asynccontextmanager
from logging import config

from fastapi import FastAPI

from dddpy.infrastructure.sqlite.database import create_tables, engine
from dddpy.presentation.api.todo.handlers.todo_api_route_handler import (
    TodoApiRouteHandler,
)

config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage database setup and teardown for the FastAPI lifespan.

    Args:
        app: FastAPI application instance invoking the lifespan context.

    Yields:
        None: Control is yielded back to FastAPI after setup completes.
    """
    create_tables()
    yield
    engine.dispose()


app = FastAPI(
    title='DDD Todo API',
    description='A RESTful API for managing todos using Domain-Driven Design principles.',
    version='2.0.3',
    lifespan=lifespan,
)

todo_route_handler = TodoApiRouteHandler()
todo_route_handler.register_routes(app)


from typing import Annotated
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str
    email: str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):     # 只有安全字段
    id: int

@app.get("/users", response_model=UserOut)
def create_user(user: UserIn):
    # 模拟落库，生成 id
    return {"id": 10, "username": user.username, "email": user.email, "password": "ignore me"}