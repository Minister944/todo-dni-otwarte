from fastapi import HTTPException


def todo_to_dict(id, description, completed):
    return {"id": id, "description": description, "completed": bool(completed)}


def get_todos(db):
    query = "SELECT id, description, completed FROM todo ORDER BY id"
    todos = []

    for todo in db.execute(query):
        todos.append(todo_to_dict(*todo))

    return todos


def create_todo(db, data):
    query = "INSERT INTO todo (description) VALUES (:description)"
    data = db.execute(query, data)

    return data.lastrowid


def update_todo(db, data):
    print(data)
    if data["description"] == None and data["completed"] == None:
        raise HTTPException(
            status_code=400,
            detail="At least one of 'description' or 'completed' must be provided",
        )

    query = "UPDATE todo SET description=COALESCE(:description, description), completed=COALESCE(:completed, completed) WHERE id=:id"
    data = db.execute(query, data)

    if data.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")


def delete_todo(db, data):
    query = "DELETE FROM todo WHERE id = :id"
    data = db.execute(query, data)

    if data.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
