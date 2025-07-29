from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    quantity: int
    date_posted: datetime

products_db: List[Product] = []

@app.get("/")
def root():
    return {"message": "Webshop API radi!"}

@app.get("/products", response_model=List[Product])
def get_products():
    return products_db

@app.post("/products", response_model=Product)
def create_product(product: Product):
    products_db.append(product)
    return product
