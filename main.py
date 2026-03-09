from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.

    Parameters:
    - a: First number
    - b: Second number

    Returns:
    JSON object containing the operation, inputs, and result.
    """

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": a + b
    }

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    Subtract the second number from the first number.

    Parameters:
    - a: first number
    - b: second number

    Returns:
    - JSON with the operation name, inputs, and result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": a - b
    }


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    Multiply two numbers and return their product.

    Parameters:
    - a: first number
    - b: second number

    Returns:
    - JSON with the operation name, inputs, and result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": a * b
    }


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    Divide the first number by the second number.

    Parameters:
    - a: dividend
    - b: divisor

    Returns:
    - JSON with the operation name, inputs, and result

    Validation:
    - b cannot be zero
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    if b == 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Division by zero is not allowed. Please provide a non-zero value for b."
        )

    return {
        "operation": "divide",
        "a": a,
        "b": b,
        "result": a / b
    }


@app.get("/power/{a}/{b}", status_code=200)
def power(a: str, b: str):
    """
    Raise the first number to the power of the second number.

    Parameters:
    - a: base
    - b: exponent

    Returns:
    - JSON with the operation name, inputs, and result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    return {
        "operation": "power",
        "a": a,
        "b": b,
        "result": a ** b
    }


@app.get("/rectangle-area/{length}/{width}", status_code=200)
def rectangle_area(length: str, width: str):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length: rectangle length
    - width: rectangle width

    Returns:
    - JSON with the operation name, inputs, and result

    Validation:
    - length and width must be non-negative
    """
    try:
        length = float(length)
        width = float(width)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    if length < 0 or width < 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Length and width must be non-negative numbers."
        )

    return {
        "operation": "rectangle-area",
        "length": length,
        "width": width,
        "result": length * width
    }


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: str, b: str, c: str):
    """
    Calculate the average of three numbers.

    Parameters:
    - a: first number
    - b: second number
    - c: third number

    Returns:
    - JSON with the operation name, inputs, and result
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="All arguments must be valid numbers."
        )

    return {
        "operation": "average",
        "a": a,
        "b": b,
        "c": c,
        "result": (a + b + c) / 3
    }