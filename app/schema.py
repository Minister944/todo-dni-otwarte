from typing import Optional
from pydantic import BaseModel


class CreateTodo(BaseModel):
    description: str


class UpdateTodo(BaseModel):
    id: int
    description: Optional[str]
    completed: Optional[bool]


class DeleteTodo(BaseModel):
    id: int
