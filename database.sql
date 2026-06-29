-- ===========================================
-- Wrong Parking Detection System Database
-- ===========================================

CREATE DATABASE IF NOT EXISTS wrong_parking_db;

USE wrong_parking_db;

-- ===========================================
-- Admin Login Table
-- ===========================================

CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO admin (username, password)
VALUES ('admin', 'admin123');

-- ===========================================
-- Vehicle Registration Table
-- ===========================================

CREATE TABLE vehicles (

    id INT AUTO_INCREMENT PRIMARY KEY,

    vehicle_number VARCHAR(20) NOT NULL UNIQUE,

    owner_name VARCHAR(100) NOT NULL,

    phone VARCHAR(15),

    vehicle_type VARCHAR(30),

    vehicle_color VARCHAR(30),

    parking_zone VARCHAR(50),

    address TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ===========================================
-- Wrong Parking History
-- ===========================================

CREATE TABLE wrong_parking (

    id INT AUTO_INCREMENT PRIMARY KEY,

    vehicle_number VARCHAR(20),

    owner_name VARCHAR(100),

    vehicle_type VARCHAR(30),

    parking_zone VARCHAR(50),

    location VARCHAR(100),

    image_path VARCHAR(255),

    detected_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    status VARCHAR(30) DEFAULT 'Wrong Parking'

);

-- ===========================================
-- Camera Log
-- ===========================================

CREATE TABLE camera_logs (

    id INT AUTO_INCREMENT PRIMARY KEY,

    camera_name VARCHAR(50),

    location VARCHAR(100),

    status VARCHAR(20),

    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ===========================================
-- Sample Vehicle Records
-- ===========================================

INSERT INTO vehicles
(vehicle_number, owner_name, phone, vehicle_type, vehicle_color, parking_zone, address)
VALUES
('TS09AB1234','Ramesh','9876543210','Car','White','Zone A','Hyderabad'),

('TS08CD5678','Suresh','9123456789','Bike','Black','Zone B','Warangal'),

('TS10EF4321','Priya','9988776655','Car','Blue','Zone C','Nizamabad'),

('TS07GH9999','Anil','9000011111','Auto','Yellow','Visitor Parking','Karimnagar');

-- ===========================================
-- Sample Wrong Parking Record
-- ===========================================

INSERT INTO wrong_parking
(vehicle_number, owner_name, vehicle_type, parking_zone, location, image_path)
VALUES
('TS09AB1234',
'Ramesh',
'Car',
'Zone A',
'College Main Gate',
'static/uploads/TS09AB1234.jpg');

-- ===========================================
-- View Registered Vehicles
-- ===========================================

SELECT * FROM vehicles;

-- ===========================================
-- View Wrong Parking History
-- ===========================================

SELECT * FROM wrong_parking;

-- ===========================================
-- View Admin Users
-- ===========================================

SELECT * FROM admin;
