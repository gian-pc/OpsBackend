from datetime import datetime

from src.domain.customer import Customer
from src.domain.product import Product

from src.interfaces.i_customer_repository import ICustomerRepository
from src.interfaces.i_order_repository import IOrderRepository
from src.interfaces.i_product_repository import IProductRepository

from src.repositories.customer_repository import CustomerRepository
from src.repositories.order_repository import OrderRepository
from src.repositories.product_repository import ProductRepository
from src.services.customer_service import CustomerService

from src.services.order_service import OrderService


class App:

    # Acoplamiento FUERTE
    # def __init__(self):
    #     self.customer_repo = CustomerRepository()
    #     self.product_repo = ProductRepository()
    #     self.order_repo = OrderRepository()

    # Acoplamiento DÉBIL
    def __init__(
            self,
            customer_repo: ICustomerRepository,
            product_repo: IProductRepository,
            order_repo: IOrderRepository
    ):
        self.customer_repo = customer_repo
        self.product_repo = product_repo
        self.order_repo = order_repo

    def run(self):
        print("=== SISTEMA DE GESTION DE PEDIDOS ===\n")

        # Crear datos de ejemplo
        self._seed_data()

        # Mostrar menú
        while True:
            print("\n--- MENÚ ---")
            print("1. Ver todos los clientes")
            print("2. Ver todos los productos")
            print("3. Ver todos los pedidos")
            print("4. Crear pedido")
            print("5. Eliminar cliente")
            print("6. Salir")

            opcion = input("\nSelecciona una opción: ")

            if opcion == "1":
                self._mostrar_clientes()
            elif opcion == "2":
                self._mostrar_productos()
            elif opcion == "3":
                self._mostrar_pedidos()
            elif opcion == "4":
                self._crear_pedido()
            elif opcion == "5":
                self._eliminar_cliente()
            elif opcion == "6":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida")

    def _seed_data(self):
        # Crear clientes iniciales
        c1 = Customer(0, "gian@email.com", "Gian PC", True, datetime.now())
        c2 = Customer(0, "maria@email.com", "Maria Lopez", True, datetime.now())
        self.customer_repo.save(c1)
        self.customer_repo.save(c2)

        # Crear productos iniciales
        p1 = Product(0, "Laptop HP", 1500.99, 10, datetime.now())
        p2 = Product(0, "Mouse Logitech", 25.50, 50, datetime.now())
        p3 = Product(0, "Teclado Mecánico", 89.99, 25, datetime.now())
        self.product_repo.save(p1)
        self.product_repo.save(p2)
        self.product_repo.save(p3)

        print("Datos iniciales cargados ✓")

    def _mostrar_clientes(self):
        print("\n=== CLIENTES ===")
        for cliente in self.customer_repo.find_all():
            estado = "✓ Activo" if cliente.is_active else "✗ Inactivo"
            print(f"ID: {cliente.id} | {cliente.name} | {cliente.email} | {estado}")

    def _mostrar_productos(self):
        print("\n=== PRODUCTOS ===")
        for producto in self.product_repo.find_all():
            print(f"ID: {producto.id} | {producto.name} | ${producto.price} | Stock: {producto.stock}")

    def _mostrar_pedidos(self):
        print("\n=== PEDIDOS ===")
        pedidos = self.order_repo.find_all()
        if not pedidos:
            print("No hay pedidos registrados")
            return

        for pedido in pedidos:
            print(f"\nPedido #{pedido.id}")
            print(f"  Cliente: {pedido.customer.name}")
            print(f"  Productos:")
            for producto in pedido.products:
                print(f"    - {producto.name} (${producto.price})")
            print(f"  Total: ${pedido.total}")

    def _crear_pedido(self):
        print("\n=== CREAR PEDIDO ===")

        # Mostrar clientes disponibles
        print("\nClientes disponibles:")
        self._mostrar_clientes()

        customer_id = int(input("\nID del cliente: "))
        cliente = self.customer_repo.find_by_id(customer_id)

        if not cliente:
            print("Cliente no encontrado")
            return

        # Mostrar productos disponibles
        print("\nProductos disponibles:")
        self._mostrar_productos()

        # Seleccionar productos
        productos_seleccionados = []
        while True:
            product_id = input("\nID del producto (o 'fin' para terminar): ")

            if product_id.lower() == 'fin':
                break

            producto = self.product_repo.find_by_id(int(product_id))
            if producto:
                productos_seleccionados.append(producto)
                print(f"✓ {producto.name} agregado")
            else:
                print("Producto no encontrado")

        # Crear el pedido usando el servicio
        try:
            pedido = OrderService.create_order(0, cliente, productos_seleccionados)
            self.order_repo.save(pedido)
            print(f"\n✓ Pedido #{pedido.id} creado exitosamente")
            print(f"Total: ${pedido.total}")
        except ValueError as e:
            print(f"\n✗ Error: {e}")

    def _eliminar_cliente(self):
        print("\n=== ELIMINAR CLIENTE ===")

        print("\nClientes disponibles:")
        self._mostrar_clientes()
        customer_id = int(input("\nID del cliente: "))

        try:
            CustomerService.delete_customer(customer_id, self.customer_repo, self.order_repo)  # ← ¿Qué parámetros van?
            print("✓ Cliente eliminado exitosamente")
        except ValueError as e:
            print(f"✗ Error: {e}")




if __name__ == "__main__":
    # app = App()
    # app.run()

    # Crear las implementaciones concretas
    customer_repo = CustomerRepository()
    product_repo = ProductRepository()
    order_repo = OrderRepository()

    # Inyectar dependencias
    app = App(customer_repo, product_repo, order_repo)
    app.run()
