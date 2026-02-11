
from datetime import datetime

from src.domain.customer import Customer
from src.domain.product import Product
from src.services.order_service import OrderService

# Crear cliente
cliente = Customer(
    id = 1,
    email = "gian@email.com",
    name="Gian PC",
    is_active = True,
    created_at = datetime.now(),
)

# Crear productos
producto1 = Product(id=101, name="Laptop HP", price=1500.99, stock=10, created_at=datetime.now())
producto2 = Product(id=102, name="Mouse", price=25.50, stock=50, created_at=datetime.now())

# Crear pedido usando el SERVICIO (calcula el total automáticamente)
pedido = OrderService.create_order(
    order_id=1001,
    customer=cliente,
    products=[producto1, producto2],
)

print("=== PEDIDO CREADO POR EL SERVICIO ===")
print(f"ID: {pedido.id}")
print(f"Cliente: {pedido.customer.name}")
print(f"Total calculado automáticamente: ${pedido.total}")
print(f"Productos: {len(pedido.products)}")

print("\n=== PRUEBA 1: Pedido sin productos ===")
try:
    pedido_vacio = OrderService.create_order(
        order_id=1002,
        customer=cliente,
        products=[]  # ← Lista vacía
    )
except ValueError as e:
    print(f"Error capturado: {e}")


print("\n=== PRUEBA 2: Cliente inactivo ===")
cliente_inactivo = Customer(
    id=2,
    email="inactivo@email.com",
    name="Usuario Inactivo",
    is_active=False,  # ← Cliente inactivo
    created_at=datetime.now()
)

try:
    pedido_invalido = OrderService.create_order(
        order_id=1003,
        customer=cliente_inactivo,
        products=[producto1]
    )
except ValueError as e:
    print(f"Error capturado: {e}")