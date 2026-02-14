# Notas SQL - Semana 2

## Día 8: SQL Básico

### SELECT - Consultar datos
```sql
-- Todas las columnas
SELECT * FROM customers;

-- Columnas específicas
SELECT name, email FROM customers;
```

### WHERE - Filtrar
```sql
-- Filtro simple
SELECT * FROM customers WHERE is_active = 1;

-- Comparaciones
SELECT * FROM products WHERE price > 100;

-- LIKE para búsqueda de texto
SELECT * FROM customers WHERE name LIKE '%ar%';

-- AND / OR
SELECT * FROM customers WHERE is_active = 1 AND name LIKE '%a%';
```

### ORDER BY - Ordenar
```sql
SELECT * FROM products ORDER BY price DESC;
SELECT * FROM products ORDER BY name ASC;
```

### LIMIT - Limitar resultados
```sql
SELECT * FROM products LIMIT 3;
SELECT * FROM products ORDER BY price DESC LIMIT 2;
```

### Funciones de agregación
```sql
SELECT COUNT(*) FROM products;
SELECT SUM(stock) FROM products;
SELECT AVG(price) FROM products;
SELECT MIN(price), MAX(price) FROM products;
```

### AS - Aliases
```sql
SELECT 
    name AS producto,
    price AS precio
FROM products;

SELECT COUNT(*) AS total FROM products;
```