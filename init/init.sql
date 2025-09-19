CREATE DATABASE IF NOT EXISTS myapp;
USE myapp;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  stock INT DEFAULT 0
);

INSERT INTO users (name, email) VALUES
('Nour', 'nour@example.com'),
('Ali', 'ali@example.com');

INSERT INTO products (name, price, stock) VALUES
('Laptop', 1500.00, 10),
('Mouse', 15.00, 50);