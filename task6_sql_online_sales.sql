CREATE TABLE online_sales (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    product_id INT NOT NULL
);

INSERT INTO online_sales (order_date, amount, product_id) VALUES
('2023-01-05', 200.50, 101),
('2023-01-15', 150.00, 102),
('2023-02-10', 300.75, 103),
('2023-02-18', 120.00, 101),
('2023-03-05', 500.00, 104),
('2023-03-22', 250.00, 102),
('2023-04-02', 100.00, 101),
('2023-04-15', 400.00, 103),
('2023-05-08', 350.00, 104),
('2023-05-20', 220.00, 102);

SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM online_sales
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year, month;

SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM online_sales
WHERE EXTRACT(YEAR FROM order_date) = 2023
GROUP BY EXTRACT(YEAR FROM order_date), EXTRACT(MONTH FROM order_date)
ORDER BY year, month;
