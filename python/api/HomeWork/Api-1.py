from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/sum1n")
def sum_1_to_n(n: int):
    # Рассчитываем сумму от 1 до n
    result = sum(range(1, n + 1))
    return {"result": result}

##################

@app.get("/fibo")
def fibonacci(n: int):
    if n < 0:
        return {"error": "n must be a non-negative integer"}
    elif n == 0:
        return {"result": 0}
    elif n == 1:
        return {"result": 1}

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return {"result": b}

#################

@app.post("/reverse")
def reverse_string(string: str = Header(None)):
    if string is None:
        raise HTTPException(status_code=400, detail="Header 'string' is required")
    reversed_string = string[::-1]
    return {"result": reversed_string}

#################
global_list = []  # Глобальный массив для хранения элементов

class Item(BaseModel):
    element: str

@app.put("/list")
def add_to_list(item: Item):
    global global_list
    global_list.append(item.element)
    return {"result": global_list}

@app.get("/list")
def get_list():
    return {"result": global_list}

############################

global_list2 = []  # Глобальный массив для хранения элементов

class Item(BaseModel):
    element: str

@app.put("/list")
def add_to_list(item: Item):
    global global_list
    global_list.append(item.element)
    return {"result": global_list}

@app.get("/list")
def get_list():
    return {"result": global_list}

##########################

class Expression(BaseModel):
    expr: str

@app.post("/calculator")
def calculate(expression: Expression):
    try:
        # Разделяем выражение на компоненты
        num1_str, operator, num2_str = expression.expr.split(",")
        
        # Преобразуем числа из строки в float
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Выполняем соответствующую операцию
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise HTTPException(status_code=403, detail={"error": "zerodiv"})
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail={"error": "invalid"})
        
        return {"result": result}
    
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": "invalid"})
    except Exception as e:
        raise HTTPException(status_code=400, detail={"error": "invalid"})

