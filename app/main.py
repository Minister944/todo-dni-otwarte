from fastapi import FastAPI
from app.crud import get_todos, create_todo, delete_todo, update_todo
from app.database import cursor
from app.schema import CreateTodo, UpdateTodo, DeleteTodo

app = FastAPI()


@app.get("/todos", tags=["todo"])
def get_all_todos():
    with cursor() as cur:
        todos = get_todos(cur)

    return todos


@app.post("/todo", status_code=201, tags=["todo"])
def add_todo(data: CreateTodo):
    with cursor() as cur:
        id = create_todo(cur, data.dict())

    return {"id": id}


@app.put("/todo", tags=["todo"])
def todo_update(data: UpdateTodo):
    with cursor() as cur:
        id = update_todo(cur, data.dict())

    return {"id": id}


@app.delete("/todo", tags=["todo"])
def del_todo(data: DeleteTodo):
    with cursor() as cur:
        delete_todo(cur, data.dict())
    return {"status": "ok"}
