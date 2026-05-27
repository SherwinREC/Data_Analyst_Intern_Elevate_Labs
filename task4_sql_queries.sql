\set QUIET 1

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    country VARCHAR(50)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2),
    stock INT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    total_amount NUMERIC(10,2)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price NUMERIC(10,2)
);

INSERT INTO customers (first_name, last_name, email, country)
SELECT * FROM (VALUES
('Arjun', 'Mehta', 'arjun.mehta@example.com', 'India'),
('Sophia', 'Williams', 'sophia.williams@example.com', 'USA'),
('Liam', 'Brown', 'liam.brown@example.com', 'UK'),
('Aditi', 'Sharma', 'aditi.sharma@example.com', 'India'),
('Oliver', 'Jones', 'oliver.jones@example.com', 'Canada')
) AS t(first_name, last_name, email, country);

INSERT INTO products (product_name, category, price, stock)
SELECT * FROM (VALUES
('Laptop', 'Electronics', 750.00, 20),
('Smartphone', 'Electronics', 500.00, 35),
('Headphones', 'Accessories', 80.00, 50),
('Office Chair', 'Furniture', 150.00, 15),
('Coffee Maker', 'Appliances', 120.00, 10)
) AS t(product_name, category, price, stock);

INSERT INTO orders (customer_id, order_date, total_amount)
SELECT * FROM (VALUES
(1, '2025-09-01'::DATE, 1250.00),
(2, '2025-09-05'::DATE, 500.00),
(3, '2025-09-10'::DATE, 80.00),
(4, '2025-09-12'::DATE, 150.00),
(5, '2025-09-15'::DATE, 870.00)
) AS t(customer_id, order_date, total_amount);

INSERT INTO order_items (order_id, product_id, quantity, price)
SELECT * FROM (VALUES
(1, 1, 1, 750.00),
(1, 2, 1, 500.00),
(2, 2, 1, 500.00),
(3, 3, 1, 80.00),
(4, 4, 1, 150.00)
) AS t(order_id, product_id, quantity, price);

SELECT customer_id, first_name, last_name, country
FROM customers
WHERE country = 'India';

SELECT product_id, product_name, price
FROM products
ORDER BY price DESC
LIMIT 10;

SELECT c.country, SUM(o.total_amount) AS total_sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.country
ORDER BY total_sales DESC;

SELECT o.order_id, c.first_name, c.last_name, o.order_date, o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC;

SELECT c.customer_id, c.first_name, o.order_id, o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

SELECT customer_id, first_name, last_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING SUM(total_amount) > (
        SELECT AVG(total_amount) FROM orders
    )
);

CREATE VIEW monthly_sales AS
SELECT DATE_TRUNC('month', order_date) AS month, SUM(total_amount) AS sales
FROM orders
GROUP BY month
ORDER BY month;

CREATE INDEX idx_orders_customer_id ON orders(customer_id);
