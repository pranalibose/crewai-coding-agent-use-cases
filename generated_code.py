from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///todo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class TodoORM(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import TodoORM

class DBConfig:
    engine = engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from typing import List, Optional

def get_todo(db: Session, todo_id: int):
    return db.query(TodoORM).filter(TodoORM.id == todo_id).first()

def get_todos(db: Session):
    return db.query(TodoORM).all()

def create_todo(db: Session, todo: TodoORM):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, todo_id: int, todo: TodoORM):
    existing_todo = get_todo(db, todo_id)
    if existing_todo:
        existing_todo.title = todo.title
        existing_todo.description = todo.description
        existing_todo.completed = todo.completed
        db.commit()
        return existing_todo
    return None

def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from database import db
from crud import get_todos, create_todo, update_todo, delete_todo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)

@app.route("/todos", methods=["GET"])
def get_all_todos():
    try:
        todos = get_todos(db)
        return jsonify([todo.__dict__ for todo in todos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/todos", methods=["POST"])
def create_new_todo():
    try:
        data = request.get_json()
        if "title" not in data or "description" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        new_todo = TodoORM(title=data["title"], description=data["description"], completed=False)
        created_todo = create_todo(db, new_todo)
        return jsonify(created_todo.__dict__)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id: int):
    try:
        todo = get_todo(db, todo_id)
        if todo:
            return jsonify(todo.__dict__)
        return jsonify({"error": "Todo not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo_by_id(todo_id: int):
    try:
        data = request.get_json()
        if "title" not in data or "description" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        updated_todo = update_todo(db, todo_id, TodoORM(title=data["title"], description=data["description"], completed=False))
        if updated_todo:
            return jsonify(updated_todo.__dict__)
        return jsonify({"error": "Todo not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo_by_id(todo_id: int):
    try:
        deleted = delete_todo(db, todo_id)
        if deleted:
            return jsonify({"message": "Todo deleted successfully"}), 200
        return jsonify({"error": "Todo not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)