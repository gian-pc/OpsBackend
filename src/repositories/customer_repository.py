from typing import List, Optional

from src.domain.customer import Customer


class CustomerRepository:

    def __init__(self):
        self._customers: List[Customer] = []
        self._next_id: int = 1

    def save(self, customer: Customer) -> Customer:
        if customer.id == 0:
            customer.id = self._next_id
            self._next_id += 1
        self._customers.append(customer)
        return customer

    def find_by_id(self, customer_id: int) -> Optional[Customer]:
        for customer in self._customers:
            if customer.id == customer_id:
                return customer
        return None

    def find_by_email(self, email: str) -> Optional[Customer]:
        for customer in self._customers:
            if customer.email == email:
                return customer
        return None

    def find_all(self) -> List[Customer]:
        return self._customers.copy()
