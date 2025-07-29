from typing import List, Optional
from datetime import datetime
from ..models.order import Order, OrderCreate, OrderStatus

class OrderService:
    def __init__(self):
        self.orders: List[Order] = []
        self.next_id = 1
    
    def get_all_orders(self, sort_by: str = "created_at", order: str = "desc") -> List[Order]:
        sorted_orders = sorted(
            self.orders,
            key=lambda x: getattr(x, sort_by),
            reverse=(order.lower() == "desc")
        )
        return sorted_orders
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return next((o for o in self.orders if o.id == order_id), None)
    
    def create_order(self, order_data: OrderCreate) -> Order:
        total_amount = sum(item.quantity * item.price for item in order_data.items)
        
        order = Order(
            id=self.next_id,
            items=order_data.items,
            customer=order_data.customer,
            status=OrderStatus.PENDING,
            created_at=datetime.now(),
            total_amount=total_amount
        )
        self.orders.append(order)
        self.next_id += 1
        return order
    
    def update_order_status(self, order_id: int, status: OrderStatus) -> Optional[Order]:
        order = self.get_order_by_id(order_id)
        if not order:
            return None
        
        order.status = status
        order.updated_at = datetime.now()
        return order