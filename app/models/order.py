from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class CustomerInfo(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone: str
    email: Optional[str] = None

class Order(BaseModel):
    id: int
    items: List[OrderItem]
    customer: CustomerInfo
    status: OrderStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    total_amount: float

class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer: CustomerInfo