from datetime import datetime

from src.domain.product import Product


class ProductService:

    @staticmethod
    def create_product(product_id: int, name: str, price:float, stock: int) -> Product:
        if price <= 0:
            raise ValueError("Price must be greater than zero")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        if not name.strip():
            raise ValueError("Product name cannot be empty")

        return Product(
            id=product_id,
            name=name,
            price=price,
            stock=stock,
            created_at=datetime.now()
        )