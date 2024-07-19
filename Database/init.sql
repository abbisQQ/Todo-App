-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS applicationdb;

-- Use the created database
USE applicationdb;

-- Create the todos table if it doesn't exist
CREATE TABLE IF NOT EXISTS todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    due_date DATE NOT NULL
);

-- Insert initial data into the todos table
INSERT INTO todos (name, description, due_date) VALUES 
('Buy groceries', 'Milk, eggs, bread, and butter', '2024-08-01'),
('Complete project', 'Finish the Flask application', '2024-07-31'),
('Call John', 'Discuss project updates', '2024-08-02');