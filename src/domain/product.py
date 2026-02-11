from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    created_at: datetime
