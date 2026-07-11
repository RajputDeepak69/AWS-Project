CREATE DATABASE IF NOT EXISTS infratrack;

USE infratrack;

CREATE TABLE IF NOT EXISTS servers (

    id INT AUTO_INCREMENT PRIMARY KEY,

    server_name VARCHAR(100) NOT NULL,

    environment ENUM('Development','Testing','Production') NOT NULL,

    operating_system VARCHAR(50) NOT NULL,

    ip_address VARCHAR(20) NOT NULL,

    owner VARCHAR(100) NOT NULL,

    status ENUM('Running','Stopped') DEFAULT 'Running',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);