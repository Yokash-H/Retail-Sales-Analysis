CREATE DATABASE superstore_db;
USE superstore_db;
CREATE TABLE superstore_dataset (
    OrderID VARCHAR(20),
    OrderDate DATE,
    ShipDate DATE,
    CustomerID VARCHAR(20),
    CustomerName VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    Region VARCHAR(50),
    ProductID VARCHAR(20),
    Category VARCHAR(50),
    SubCategory VARCHAR(50),
    ProductName VARCHAR(50),
    Sales FLOAT,
    Quantity INT,
    Discount FLOAT,
    Profit FLOAT
);