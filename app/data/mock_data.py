from typing import List
from ..models.product import ProductCreate
from ..models.order import OrderCreate, OrderItem, CustomerInfo

# Mock Products Data
MOCK_PRODUCTS: List[ProductCreate] = [
    ProductCreate(
        name="Laptop HP Pavilion",
        description="High-performance laptop perfect for work and gaming. Intel i7 processor, 16GB RAM, 512GB SSD.",
        price=999.99,
        image_url="https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&h=300&fit=crop",
        quantity=10
    ),
    ProductCreate(
        name="Smartphone Samsung Galaxy",
        description="Latest Android smartphone with amazing camera, 128GB storage, and long-lasting battery.",
        price=599.99,
        image_url="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop",
        quantity=25
    ),
    ProductCreate(
        name="Wireless Headphones Sony",
        description="Premium noise-cancelling wireless headphones with 30-hour battery life.",
        price=199.99,
        image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop",
        quantity=15
    ),
    ProductCreate(
        name="Gaming Mouse Logitech",
        description="Professional gaming mouse with RGB lighting and customizable buttons.",
        price=79.99,
        image_url="https://images.unsplash.com/photo-1527814050087-3793815479db?w=400&h=300&fit=crop",
        quantity=30
    ),
    ProductCreate(
        name="Mechanical Keyboard",
        description="RGB mechanical keyboard with blue switches, perfect for gaming and typing.",
        price=129.99,
        image_url="https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=400&h=300&fit=crop",
        quantity=20
    ),
    ProductCreate(
        name="Apple MacBook Air M2",
        description="Ultra-thin laptop with Apple M2 chip, 8GB RAM, 256GB SSD. Perfect for professionals and students.",
        price=1199.99,
        image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&h=300&fit=crop",
        quantity=8
    ),
    ProductCreate(
        name="iPhone 14 Pro",
        description="Latest iPhone with A16 Bionic chip, Pro camera system, and Dynamic Island.",
        price=1099.99,
        image_url="https://images.unsplash.com/photo-1678652197831-2d180705cd2c?w=400&h=300&fit=crop",
        quantity=12
    ),
    ProductCreate(
        name="iPad Pro 11-inch",
        description="Powerful tablet with M2 chip, Liquid Retina display, and Apple Pencil support.",
        price=799.99,
        image_url="https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400&h=300&fit=crop",
        quantity=18
    ),
    ProductCreate(
        name="Dell XPS 13",
        description="Premium ultrabook with Intel i7, 16GB RAM, 512GB SSD, and stunning 4K display.",
        price=1299.99,
        image_url="https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=400&h=300&fit=crop",
        quantity=6
    ),
    ProductCreate(
        name="Nintendo Switch OLED",
        description="Handheld gaming console with vibrant OLED screen and Joy-Con controllers.",
        price=349.99,
        image_url="https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400&h=300&fit=crop",
        quantity=22
    ),
    ProductCreate(
        name="AirPods Pro 2nd Gen",
        description="Active noise cancellation earbuds with spatial audio and adaptive transparency.",
        price=249.99,
        image_url="https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400&h=300&fit=crop",
        quantity=35
    ),
    ProductCreate(
        name="Samsung 4K Smart TV 55\"",
        description="Crystal UHD 4K Smart TV with HDR, built-in streaming apps, and voice control.",
        price=549.99,
        image_url="https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400&h=300&fit=crop",
        quantity=14
    ),
    ProductCreate(
        name="PS5 DualSense Controller",
        description="Wireless controller with haptic feedback, adaptive triggers, and built-in microphone.",
        price=69.99,
        image_url="https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400&h=300&fit=crop",
        quantity=40
    ),
    ProductCreate(
        name="Canon EOS R6 Camera",
        description="Full-frame mirrorless camera with 20MP sensor, 4K video, and image stabilization.",
        price=2499.99,
        image_url="https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=400&h=300&fit=crop",
        quantity=5
    ),
    ProductCreate(
        name="Fitbit Charge 5",
        description="Advanced fitness tracker with GPS, heart rate monitoring, and 7-day battery life.",
        price=179.99,
        image_url="https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=400&h=300&fit=crop",
        quantity=28
    ),
    ProductCreate(
        name="Amazon Echo Dot 5th Gen",
        description="Smart speaker with Alexa, improved sound quality, and temperature sensor.",
        price=49.99,
        image_url="https://images.unsplash.com/photo-1543512214-318c7553f230?w=400&h=300&fit=crop",
        quantity=50
    ),
    ProductCreate(
        name="Google Pixel 7 Pro",
        description="Android smartphone with Google Tensor G2, advanced camera AI, and 5G connectivity.",
        price=899.99,
        image_url="https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400&h=300&fit=crop",
        quantity=16
    ),
    ProductCreate(
        name="Surface Pro 9",
        description="2-in-1 laptop/tablet with Intel i7, 16GB RAM, and detachable keyboard.",
        price=1299.99,
        image_url="https://images.unsplash.com/photo-1542393545-10f5cde2c810?w=400&h=300&fit=crop",
        quantity=9
    ),
    ProductCreate(
        name="Razer DeathAdder V3",
        description="Pro esports gaming mouse with Focus Pro 30K sensor and ergonomic design.",
        price=89.99,
        image_url="https://images.unsplash.com/photo-1563297007-0686b7003af7?w=400&h=300&fit=crop",
        quantity=24
    ),
    ProductCreate(
        name="LG UltraWide 34\" Monitor",
        description="34-inch curved ultrawide monitor with QHD resolution and USB-C connectivity.",
        price=449.99,
        image_url="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=400&h=300&fit=crop",
        quantity=11
    ),
    ProductCreate(
        name="Bose QuietComfort 45",
        description="World-class noise cancelling headphones with 24-hour battery life.",
        price=329.99,
        image_url="https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&h=300&fit=crop",
        quantity=19
    ),
    ProductCreate(
        name="JBL Flip 6 Speaker",
        description="Portable Bluetooth speaker with powerful sound and IP67 waterproof rating.",
        price=129.99,
        image_url="https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400&h=300&fit=crop",
        quantity=33
    ),
    ProductCreate(
        name="Anker PowerCore 10000",
        description="Compact portable charger with 10,000mAh capacity and fast charging technology.",
        price=29.99,
        image_url="https://images.unsplash.com/photo-1609592542823-8265874de38c?w=400&h=300&fit=crop",
        quantity=45
    ),
    ProductCreate(
        name="Corsair K95 RGB Platinum",
        description="Premium mechanical gaming keyboard with Cherry MX switches and RGB lighting.",
        price=199.99,
        image_url="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&h=300&fit=crop",
        quantity=13
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