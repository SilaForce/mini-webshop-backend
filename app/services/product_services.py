from typing import List, Optional
from datetime import datetime
from ..models.product import Product, ProductCreate, ProductUpdate

class ProductService:
    def __init__(self):
        self.products: List[Product] = []
        self.next_id = 1
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with some sample products for testing"""
        sample_products = [
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
        
        for product_data in sample_products:
            self.create_product(product_data)
    
    def get_all_products(self, sort_by: str = "date_posted", order: str = "desc") -> List[Product]:
        sorted_products = sorted(
            self.products,
            key=lambda x: getattr(x, sort_by),
            reverse=(order.lower() == "desc")
        )
        return sorted_products
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return next((p for p in self.products if p.id == product_id), None)
    
    def create_product(self, product_data: ProductCreate) -> Product:
        product = Product(
            id=self.next_id,
            **product_data.dict(),
            date_posted=datetime.now()
        )
        self.products.append(product)
        self.next_id += 1
        return product
    
    def update_product(self, product_id: int, product_data: ProductUpdate) -> Optional[Product]:
        product = self.get_product_by_id(product_id)
        if not product:
            return None
        
        update_data = product_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(product, field, value)
        
        return product
    
    def delete_product(self, product_id: int) -> bool:
        product = self.get_product_by_id(product_id)
        if product:
            self.products.remove(product)
            return True
        return False