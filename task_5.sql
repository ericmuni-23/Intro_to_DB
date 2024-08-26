-- Insert a single row into the Customers table
USE $1;
INSERT INTO CUSTOMER (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
-- Replace $1 with the actual database name
