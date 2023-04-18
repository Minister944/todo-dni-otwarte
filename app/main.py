from fastapi import FastAPI
from app.crud import get_todos, create_todo, delete_todo, update_todo, get_todo_by_id
from app.database import cursor
from app.schema import CreateTodo, UpdateTodo, DeleteTodo

app = FastAPI()


@app.get("/todos", tags=["todo"])
def get_all_todos():
    with cursor() as cur:
        todos = get_todos(cur)
    return todos


@app.get("/todos/{id}", tags=["todo"])
def get_todo_with_specific_id(id: int):
    with cursor() as cur:
        todo = get_todo_by_id(cur, id)
    return todo


@app.post("/todo", status_code=201, tags=["todo"])
def add_todo(data: CreateTodo):
    with cursor() as cur:
        todo = create_todo(cur, data.dict())
    return todo


@app.put("/todo/{id}", tags=["todo"])
def todo_update(data: UpdateTodo, id: int):
    with cursor() as cur:
        todo = update_todo(cur, data.dict() | {"id": id})
    return todo


@app.delete("/todo/{id}", tags=["todo"])
def del_todo(id: int):
    with cursor() as cur:
        delete_todo(cur, {"id": id})
    return {"status": "ok"}
