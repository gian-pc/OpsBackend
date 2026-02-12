from datetime import datetime
from src.domain.customer import Customer

# Crea dos clientes con los mismos datos
cliente1 = Customer(1, "test@email.com", "Test", True, datetime(2024, 1, 1))
cliente2 = Customer(1, "test@email.com", "Test", True, datetime(2024, 1, 1))

# Prueba esto:
print(cliente1 == cliente2)  # ¿Qué sale?
print(cliente1 is cliente2)  # ¿Qué sale? ¿Por qué es diferente?

# Ahora cambia un valor
cliente2.email = "test@email.com"
print(cliente1 == cliente2)  # ¿Qué sale ahora?