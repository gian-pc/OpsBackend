from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.order import Order


class IOrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> Order:
        pass

    @abstractmethod
    def find_by_id(self, order_id: int) -> Optional[Order]:
        pass

    @abstractmethod
    def find_by_customer_id(self, customer_id: int) -> List[Order]:
        pass

    @abstractmethod
    def find_all(self) -> List[Order]:
        pass