from src.interfaces.i_customer_repository import ICustomerRepository
from src.interfaces.i_order_repository import IOrderRepository


class CustomerService:

    @staticmethod
    def delete_customer(customer_id: int,customer_repo:ICustomerRepository, order_repo: IOrderRepository) -> None:
        # Si el cliente no existe
        if not customer_repo.find_by_id(customer_id):
            raise ValueError("Customer not found")

        # Si el cliente tiene pedidos
        if order_repo.find_by_customer_id(customer_id):
            raise ValueError("Cannot delete customer with existing orders")

        # Eliminar cliente
        customer_repo.delete(customer_id)




