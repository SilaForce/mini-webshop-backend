from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    quantity: int
    date_posted: datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    quantity: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    quantity: Optional[int] = None