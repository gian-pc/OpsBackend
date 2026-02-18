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

## Día 9: JOINs

### INNER JOIN - Solo registros con coincidencia
```sql
SELECT orders.id, customers.name, orders.total
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id;
```

### LEFT JOIN - Todos los registros de la tabla izquierda
```sql
SELECT customers.name, orders.id, orders.total
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
```

### JOIN + GROUP BY - Estadísticas por grupo
```sql
SELECT 
    customers.name AS cliente,
    COUNT(orders.id) AS total_pedidos,
    SUM(orders.total) AS monto_total
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id, customers.name;
```

## Día 10: HAVING y Subqueries

### HAVING - Filtrar grupos
```sql
-- Clientes con más de 1 pedido
SELECT customers.name, COUNT(orders.id) AS total_pedidos
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
HAVING COUNT(orders.id) > 1;
```

### Subquery en HAVING
```sql
-- Clientes que gastaron más que el promedio
SELECT customers.name, SUM(orders.total) AS monto_total
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id
HAVING SUM(orders.total) > (SELECT AVG(total) FROM orders);
```

### Subquery en SELECT
```sql
-- Comparar con promedio
SELECT 
    customers.name,
    SUM(orders.total) AS monto,
    (SELECT AVG(total) FROM orders) AS promedio
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id;
```