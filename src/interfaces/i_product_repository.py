from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.product import Product


class IProductRepository(ABC):

    @abstractmethod
    def save(self, product: Product) -> Product:
        pass

    @abstractmethod
    def find_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def find_all(self) -> List[Product]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> List[Product]:
        pass