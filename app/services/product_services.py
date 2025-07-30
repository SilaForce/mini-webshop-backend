from typing import List, Optional
from datetime import datetime
from ..models.product import Product, ProductCreate, ProductUpdate
from ..data.mock_data import MOCK_PRODUCTS
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import settings

class ProductService:
    def __init__(self):
        self.products: List[Product] = []
        self.next_id = 1
        if settings.USE_MOCK_DATA:
            self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with mock data"""
        for product_data in MOCK_PRODUCTS:
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