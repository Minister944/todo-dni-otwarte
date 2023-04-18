import React from "react";

import "./base.css";

import { createRoot } from "react-dom/client";
import { Button } from "./components/Button";

const App = () => {
  const [newTodo, setNewTodo] = React.useState("");
  const [todos, setTodos] = React.useState([]);

  const createTodo = async () => {
    if (newTodo) {
      const response = await fetch("http://127.0.0.1:8000/todo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description: newTodo }),
      });

      if (response.ok) {
        const data = await response.json();
        setTodos((todos) => [...todos, { ...data, description: newTodo }]);
        setNewTodo("");
      }
    }
  };

  const retrieveTodos = async () => {
    const response = await fetch("http://127.0.0.1:8000/todos");
    const data = await response.json();

    setTodos(data);
  };

  const updateTodo = async (id, completed, description) => {
    const response = await fetch(`http://127.0.0.1:8000/todo/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id, completed, description }),
    });

    if (response.ok) {
      const newTodos = [...todos];
      const idx = newTodos.findIndex((todo) => todo.id === id);
      newTodos[idx].completed = completed;

      setTodos(newTodos);
    }
  };

  const deleteTodo = async (id) => {
    const response = await fetch(`http://127.0.0.1:8000/todo/${id}`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: id }),
    });

    if (response.ok) {
      setTodos((todos) => todos.filter((todo) => todo.id !== id));
    }
  };

  React.useEffect(() => {
    retrieveTodos();
  }, []);

  return (
    <div className={"container"}>
      <div className="add-todo-form">
        <h2>Add todo</h2>
        <input
          type="text"
          value={newTodo}
          onChange={(evt) => setNewTodo(evt.target.value)}
          placeholder="Dodaj nowe zadanie..."
          data-testid="add-new-input"
        />

        <Button
          disabled={!newTodo}
          label="Dodaj"
          type="submit"
          name="todo-add"
          onClick={createTodo}
          data-testid="add-new-btn"
        />
      </div>

      {todos.map((todo) => (
        <div key={todo.id} className="grid" data-testid="todo-item">
          <span
            style={{ textDecoration: todo.completed ? "line-through" : "none" }}
            data-testid="todo-description"
          >
            {todo.description}
          </span>

          <Button
            label="Done"
            name="todo-complete"
            data-testid="todo-complete-btn"
            disabled={todo.completed}
            onClick={() =>
              updateTodo(todo.id, !todo.completed, todo.description)
            }
          />

          <Button
            name="todo-delete"
            onClick={() => deleteTodo(todo.id)}
            data-testid="todo-delete-btn"
            label="Delete"
          />
        </div>
      ))}
    </div>
  );
};

const rootNode = document.getElementById("root");
const root = createRoot(rootNode);

root.render(<App />);
