from datetime import datetime

from src.domain.customer import Customer
from src.domain.order import Order
from src.domain.product import Product

# 1. Crear un cliente
cliente = Customer(
    id=1,
    email="gian@email.com",
    name="Gian PC",
    is_active=True,
    created_at=datetime.now(),
)

# 2. Crear productos
producto1 = Product(
    id=101,
    name="Laptop HP",
    price=1500.99,
    stock=10,
    created_at=datetime.now(),
)
producto2 = Product(
    id=102,
    name="Mouse Logitech",
    price=25.50,
    stock=50,
    created_at=datetime.now(),
)

# 3. Crear un pedido con el cliente y los productos
pedido = Order(
    id=1001,
    customer=cliente,
    products=[producto1, producto2],
    total=1526.49,
    created_at=datetime.now(),
)

# 4. Imprimir todo
print("=== PEDIDO COMPLETO ===")
print(pedido)
print()
print("=== CLIENTE DEL PEDIDO ===")
print(pedido.customer.name)
print(pedido.customer.email)
print()
print("=== PRODUCTOS DEL PEDIDO ===")
for producto in pedido.products:
    print(f"- {producto.name}: ${producto.price}")

print()
print("=== EXPERIMENTO ===")
print(f"¿Cuántos productos tiene el pedido? {len(pedido.products)}")
print(f"Primer producto: {pedido.products[0].name}")
print(f"Segundo producto: {pedido.products[1].name}")