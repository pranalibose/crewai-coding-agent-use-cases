from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    """Todo model."""
    id: int
    title: str
    completed: bool

# In-memory database (replace with a real database in a production environment)
todo_id = 1
todos = [
    Todo(id=todo_id, title="Buy milk", completed=False),
]

# Get all todos
@app.get("/todos/", response_model=List[Todo])
async def readTodos():
    """
    Get all todos.

    Returns:
        List[Todo]: A list of Todo objects.
    """
    if not todos:
        raise HTTPException(status_code=404, detail="No todos found")
    return todos.copy()

# Get a specific todo
@app.get("/todos/{todo_id}", response_model=Todo)
async def readTodo(todo_id: int):
    """
    Get a specific todo.

    Args:
        todo_id (int): The ID of the todo.

    Returns:
        Todo: A Todo object.

    Raises:
        HTTPException: If the todo is not found.
    """
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Create a new todo
@app.post("/todos/", response_model=Todo)
async def createTodo(title: str):
    """
    Create a new todo.

    Args:
        title (str): The title of the todo.

    Returns:
        Todo: A Todo object.
    """
    global todo_id
    todo_id += 1
    todo = Todo(id=todo_id, title=title, completed=False)
    todos.append(todo)
    return todo

# Update a todo
@app.put("/todos/{todo_id}", response_model=Todo)
async def updateTodo(todo_id: int, title: str | None = None, completed: bool | None = None):
    """
    Update a todo.

    Args:
        todo_id (int): The ID of the todo.
        title (str | None): The new title (optional).
        completed (bool | None): Whether the todo is completed (optional).

    Returns:
        Todo: An updated Todo object.

    Raises:
        HTTPException: If the todo is not found.
    """
    for todo in todos:
        if todo.id == todo_id:
            if title:
                todo.title = title
            if completed is not None:
                todo.completed = completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete a todo
@app.delete("/todos/{todo_id}")
async def deleteTodo(todo_id: int):
    """
    Delete a todo.

    Args:
        todo_id (int): The ID of the todo.

    Returns:
        str: A success message.
    """
    global todo_id
    for todo in todos[:]:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)