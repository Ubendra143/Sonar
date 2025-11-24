from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}


@app.get("/sqrt")
def sqrt(x: float):
    if x < 0:
        raise HTTPException(status_code=400, detail="Cannot take sqrt of negative number")
    return {"result": x ** 0.5}
