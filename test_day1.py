from datetime import datetime
from src.domain.customer import Customer


# Crear un cliente
cliente1 = Customer(
    id=1,
    email="gian@email.com",
    name="Gian PC",
    is_active=True,
    created_at=datetime.now()
)

# Imprimir el cliente
print(cliente1)
print()

# Acceder a los campos
print(f"ID: {cliente1.id}")
print(f"Email: {cliente1.email}")
print(f"Nombre: {cliente1.name}")
print(f"Activo: {cliente1.is_active}")
print(f"Creado: {cliente1.created_at}")