# main.py
# FastAPI application for addition of two numbers
from fastapi import FastAPI, Body, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    """Define a Pydantic model for the request data"""
    number1: float
    number2: float

@app.post("/add/")
def add_numbers(numbers: Number):
    """
    End point to add two numbers.

    Args:
    - number1 (float): The first number.
    - number2 (float): The second number.

    Returns:
    - The sum of the two numbers.

    Raises:
    - HTTPException: If the request data is invalid.
    """
    try:
        result = numbers.number1 + numbers.number2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid request data")

# Usage Example:
# Use POST method and provide two numbers in the request body.
# API URL: /add/
# API Request Body:
# {
#     "number1": 10,
#     "number2": 20
# }