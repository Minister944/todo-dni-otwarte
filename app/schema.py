from pydantic import BaseModel


class CreateTodo(BaseModel):
    description: str


class UpdateTodo(BaseModel):
    id: int
    description: str


class DeleteTodo(BaseModel):
    id: int
