
from typing import List, Optional
from src.domain.order import Order

class OrderRepository:

    def __init__(self):
        self.orders: List[Order] = []
        self._next_id: int = 1

    def save(self, order: Order) -> Order:
        if order.id == 0:
            order.id = self._next_id
            self._next_id += 1
        self.orders.append(order)
        return order

    def find_by_id(self, order_id: int) -> Optional[Order]:
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def find_by_customer_id(self, customer_id: int) -> List[Order]:
        result = []
        for order in self.orders:
            if order.customer.id == customer_id:
                result.append(order)
        return result

    def find_all(self) -> List[Order]:
        return self.orders.copy()