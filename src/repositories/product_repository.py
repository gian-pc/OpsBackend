from typing import List, Optional

from src.domain.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []
        self._next_id: int = 1

    def save(self, product: Product) -> Product:
        if product.id == 0:
            product.id = self._next_id
            self._next_id += 1
        self.products.append(product)
        return product

    def find_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def find_all(self) -> List[Product]:
        return self.products.copy()

    def find_by_name(self, name: str) -> List[Product]:
        result = []
        for product in self.products:
            if name.lower() == product.name.lower():
                result.append(product)
        return result

