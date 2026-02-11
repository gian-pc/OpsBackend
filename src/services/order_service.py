from datetime import datetime
from typing import List

from src.domain.customer import Customer
from src.domain.order import Order
from src.domain.product import Product


class OrderService:

    @staticmethod
    def calculate_total(products: List[Product]) -> float:
        total = 0.0
        for product in products:
            total += product.price
        return total

    @staticmethod
    def create_order(order_id: int, customer: Customer, products: List[Product]) -> Order:
        if not products:
            raise ValueError("Order must have at least one product")

        if not customer.is_active:
            raise ValueError("Cannot create an order with an inactive customer")

        total = OrderService.calculate_total(products)

        return Order(id=order_id, customer=customer, products=products, total=total, created_at=datetime.now())
