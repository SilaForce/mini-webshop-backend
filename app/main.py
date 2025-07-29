from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings

from .services.product_services import ProductService
from .services.order_service import OrderService
from .services.auth_service import AuthService
from .models.product import Product, ProductCreate, ProductUpdate
from .models.order import Order, OrderCreate, OrderStatus
from .models.user import UserLogin, UserResponse

app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

product_service = ProductService()
order_service = OrderService()
auth_service = AuthService()

security = HTTPBearer()

def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if not auth_service.verify_admin_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return auth_service.get_current_user(token)

@app.get("/")
def root():
    return {"message": "Mini WebShop API is running!", "version": settings.API_VERSION}


@app.post("/auth/login")
def login(user_data: UserLogin):
    token = auth_service.authenticate_user(user_data.username, user_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return {"access_token": token, "token_type": "bearer"}

@app.get("/auth/me", response_model=UserResponse)
def get_current_user_info(current_user: dict = Depends(get_current_admin)):
    return UserResponse(username=current_user["username"])

@app.get("/products", response_model=List[Product])
def get_products(sort_by: str = "date_posted", order: str = "desc"):
    return product_service.get_all_products(sort_by=sort_by, order=order)

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Admin product endpoints (require authentication)
@app.post("/admin/products", response_model=Product)
def create_product(product_data: ProductCreate, current_user: dict = Depends(get_current_admin)):
    return product_service.create_product(product_data)

@app.put("/admin/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_data: ProductUpdate, current_user: dict = Depends(get_current_admin)):
    product = product_service.update_product(product_id, product_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/admin/products/{product_id}")
def delete_product(product_id: int, current_user: dict = Depends(get_current_admin)):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# Order endpoints (public for creating orders)
@app.post("/orders", response_model=Order)
def create_order(order_data: OrderCreate):
    return order_service.create_order(order_data)

# Admin order endpoints (require authentication)
@app.get("/admin/orders", response_model=List[Order])
def get_orders(sort_by: str = "created_at", order: str = "desc", current_user: dict = Depends(get_current_admin)):
    return order_service.get_all_orders(sort_by=sort_by, order=order)

@app.get("/admin/orders/{order_id}", response_model=Order)
def get_order(order_id: int, current_user: dict = Depends(get_current_admin)):
    order = order_service.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/admin/orders/{order_id}/status")
def update_order_status(order_id: int, status: OrderStatus, current_user: dict = Depends(get_current_admin)):
    order = order_service.update_order_status(order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": f"Order status updated to {status.value}", "order": order}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)