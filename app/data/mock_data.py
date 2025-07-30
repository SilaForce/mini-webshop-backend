from typing import List
from ..models.product import ProductCreate
from ..models.order import OrderCreate, OrderItem, CustomerInfo

# Mock Products Data
MOCK_PRODUCTS: List[ProductCreate] = [
    ProductCreate(
        name="Laptop HP Pavilion",
        description="High-performance laptop perfect for work and gaming. Intel i7 processor, 16GB RAM, 512GB SSD.",
        price=999.99,
        image_url="https://via.placeholder.com/400x300?text=Laptop+HP",
        quantity=10
    ),
    ProductCreate(
        name="Smartphone Samsung Galaxy",
        description="Latest Android smartphone with amazing camera, 128GB storage, and long-lasting battery.",
        price=599.99,
        image_url="https://via.placeholder.com/400x300?text=Samsung+Phone",
        quantity=25
    ),
    ProductCreate(
        name="Wireless Headphones Sony",
        description="Premium noise-cancelling wireless headphones with 30-hour battery life.",
        price=199.99,
        image_url="https://via.placeholder.com/400x300?text=Sony+Headphones",
        quantity=15
    ),
    ProductCreate(
        name="Gaming Mouse Logitech",
        description="Professional gaming mouse with RGB lighting and customizable buttons.",
        price=79.99,
        image_url="https://via.placeholder.com/400x300?text=Gaming+Mouse",
        quantity=30
    ),
    ProductCreate(
        name="Mechanical Keyboard",
        description="RGB mechanical keyboard with blue switches, perfect for gaming and typing.",
        price=129.99,
        image_url="https://via.placeholder.com/400x300?text=Keyboard",
        quantity=20
    )
]

MOCK_ORDERS: List[OrderCreate] = [
    OrderCreate(
        items=[
            OrderItem(product_id=1, quantity=1, price=999.99),
            OrderItem(product_id=4, quantity=2, price=79.99)
        ],
        customer=CustomerInfo(
            first_name="John",
            last_name="Doe",
            address="123 Main St, City, State",
            phone="+1234567890",
            email="john.doe@example.com"
        )
    )
]