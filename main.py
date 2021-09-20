from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Halo apa kabar"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int) -> int:
    return num1+num2
