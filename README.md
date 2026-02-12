# OpsBackend

Backend & AI training project - Sistema de gestión de operaciones para SaaS

## Stack
- Python 3.14
- FastAPI (próximamente)
- PostgreSQL (próximamente)
- LangChain (próximamente)
- Docker (próximamente)
- AWS (próximamente)

## Arquitectura actual
```
src/
├── domain/           # Entidades y contratos
│   ├── customer.py
│   ├── product.py
│   ├── order.py
│   └── interfaces/   # Interfaces (ABC)
├── services/         # Lógica de negocio
│   ├── customer_service.py
│   ├── order_service.py
│   └── product_service.py
├── repositories/     # Acceso a datos (memoria)
│   ├── customer_repository.py
│   ├── product_repository.py
│   └── order_repository.py
└── core/            # Configuraciones (vacío)
```

## Funcionalidades actuales
- ✅ Gestión de clientes (crear, listar, eliminar con validaciones)
- ✅ Gestión de productos (crear, listar, buscar)
- ✅ Gestión de pedidos (crear con cálculo automático de total)
- ✅ Validaciones de negocio (cliente activo, productos mínimos)
- ✅ Sistema interactivo por consola

## Principios aplicados
- Single Responsibility Principle (SRP)
- Dependency Inversion Principle (DIP)
- Dependency Injection
- Repository Pattern
- Arquitectura en capas

## Progreso
- [x] **Semana 1: Python puro + Arquitectura limpia** ✅
  - [x] Día 1: Estructura + Customer (dataclass)
  - [x] Día 2: Product + Order (relaciones)
  - [x] Día 3: Servicios (lógica de negocio)
  - [x] Día 4: Repositorios (patrón Repository)
  - [x] Día 5: Aplicación interactiva
  - [x] Día 6: Refactorización + DIP
  - [x] Día 7: Evaluación (eliminar cliente)
- [ ] Semana 2: SQL + PostgreSQL + Base de datos
- [ ] Semana 3: FastAPI profesional + Testing
- [ ] Semana 4: Docker + Deploy + RAG

## Cómo ejecutar
```bash
python main.py
```