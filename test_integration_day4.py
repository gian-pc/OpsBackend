from datetime import datetime
from src.domain.customer import Customer
from src.domain.product import Product
from src.repositories.customer_repository import CustomerRepository
from src.repositories.product_repository import ProductRepository
from src.repositories.order_repository import OrderRepository
from src.services.order_service import OrderService


# Crear repositorios
customer_repo = CustomerRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()

# Crear y guardar clientes
cliente1 = Customer(0, "gian@email.com", "Gian PC", True, datetime.now())
cliente2 = Customer(0, "maria@email.com", "Maria Lopez", True, datetime.now())
customer_repo.save(cliente1)
customer_repo.save(cliente2)

# Crear y guardar productos
producto1 = Product(0, "Laptop HP", 1500.99, 10, datetime.now())
producto2 = Product(0, "Mouse Logitech", 25.50, 50, datetime.now())
producto3 = Product(0, "Teclado Mecánico", 89.99, 25, datetime.now())
product_repo.save(producto1)
product_repo.save(producto2)
product_repo.save(producto3)

# Crear pedido usando el servicio
pedido1 = OrderService.create_order(0, cliente1, [producto1, producto2])
pedido2 = OrderService.create_order(0, cliente1, [producto3])
pedido3 = OrderService.create_order(0, cliente2, [producto1, producto3])

# Guardar pedidos en el repositorio
order_repo.save(pedido1)
order_repo.save(pedido2)
order_repo.save(pedido3)

# Consultas
print("=== TODOS LOS PEDIDOS ===")
for pedido in order_repo.find_all():
    print(f"Pedido #{pedido.id} | Cliente: {pedido.customer.name} | Total: ${pedido.total}")

print("\n=== PEDIDOS DE GIAN ===")
pedidos_gian = order_repo.find_by_customer_id(cliente1.id)
for pedido in pedidos_gian:
    print(f"Pedido #{pedido.id} | Total: ${pedido.total}")

print(f"\nTotal de pedidos de Gian: {len(pedidos_gian)}")