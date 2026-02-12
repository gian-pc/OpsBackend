from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.customer import Customer


class ICustomerRepository(ABC):

    @abstractmethod
    def save(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def find_by_id(self, customer_id: int) -> Optional[Customer]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Customer]:
        pass

    @abstractmethod
    def find_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def delete(self, customer_id: int) -> bool:
        pass