CREATE DATABASE pythonTutorials;
DROP TABLE Products;
CREATE TABLE Products(
	productId SERIAL PRIMARY KEY,
	productName VARCHAR,
	year INT
);

INSERT INTO Products(productName, year) 
VALUES('iphone X', 2018);
SELECT * FROM Products;

ALTER TABLE Products 
ADD CONSTRAINT PK_UniqueName
UNIQUE(productName);