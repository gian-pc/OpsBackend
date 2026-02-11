from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.domain.customer import Customer
from src.domain.product import Product

@dataclass
class Order:
    id: int
    customer: Customer
    products: List[Product]
    total: float
    created_at: datetime