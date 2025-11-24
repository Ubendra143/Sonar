from fastapi import FastAPI
import math

app = FastAPI()

secret_key = "123456"   # Hardcoded secret (security issue)

# Unused variable
temp_value = 42


@app.get("/add")
def add(a: float = 0, b: float = 0):
    # Duplicate logic (copy-paste problem)
    c = a + b
    d = a + b
    result = c  # ignoring d
    return {"result": result}


@app.get("/subtract")
def subtract(a: float, b: float):
    # Bug: wrong operation (should be a - b)
    return {"result": a + b}  # Incorrect


@app.get("/multiply")
def multiply(a: float, b: float):
    if a == 0 or b == 0:  
        # Bad practice: misleading error
        return {"error": "Zero is not allowed in multiplication"}  
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    # Bug: does not check division by zero
    try:
        return {"result": a / b}
    except:
        # Catch-all exception (bad practice)
        return {"error": "Something went wrong"}


@app.get("/sqrt")
def sqrt(x: float):
    # Bug: math domain error not handled properly
    return {"result": math.sqrt(x)}
