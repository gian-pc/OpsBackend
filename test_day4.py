from datetime import datetime

from src.domain.customer import Customer
from src.repositories.customer_repository import CustomerRepository

# Crear el repositorio
repo = CustomerRepository()

# Crear y guardar clientes
cliente1 = Customer(
    id=0, # <-- El repo asignará el ID automáticamente
    email="gian@email.com",
    name="Gian PC",
    is_active=True,
    created_at=datetime.now(),
)

cliente2 = Customer(
    id=0,
    email="maria@email.com",
    name="Maria Lopez",
    is_active=True,
    created_at=datetime.now(),
)

# Guardar en el repositorio
repo.save(cliente1)
repo.save(cliente2)

print("=== TODOS LOS CLIENTES ===")
for cliente in repo.find_all():
    print(f"ID: {cliente.id} | Email: {cliente.email} | Nombre: {cliente.name}")

print("\n=== BUSCAR POR ID ===")
encontrado = repo.find_by_id(1)
if encontrado:
    print(f"Encontrado: {encontrado.name}")

print("\n=== BUSCAR POR EMAIL ===")
encontrado = repo.find_by_email("maria@email.com")
if encontrado:
    print(f"Encontrado: {encontrado.name}")

print("\n=== BUSCAR INEXISTENTE ===")
no_existe = repo.find_by_id(999)
print(f"Resultado: {no_existe}")