from typing import Optional
from pydantic import BaseModel


class CreateTodo(BaseModel):
    description: str


class UpdateTodo(BaseModel):
    description: Optional[str]
    completed: Optional[bool]
