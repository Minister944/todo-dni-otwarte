from fastapi import HTTPException


def todo_to_dict(id, description):
    return {"id": id, "description": description}


def get_todos(db):
    query = "SELECT id, description FROM todo ORDER BY id"
    todos = []

    for todo in db.execute(query):
        todos.append(todo_to_dict(*todo))

    return todos


def create_todo(db, data):
    query = "INSERT INTO todo (description) VALUES (:description)"
    data = db.execute(query, data)

    return data.lastrowid


def update_todo(db, data):
    query = "UPDATE todo SET description=:description WHERE id=:id"
    data = db.execute(query, data)

    if data.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")


def delete_todo(db, data):
    query = "DELETE FROM todo WHERE id = :id"

    data = db.execute(query, data)

    if data.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
