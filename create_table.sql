-- "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"

CREATE TABLE transactions (
	InvoiceNo VARCHAR(20),
	StockCode VARCHAR(20),
	Description VARCHAR(100),
	Quantity INTEGER,
	InvoiceDate DATETIME,
	UnitPrice FLOAT,
	CustomerID VARCHAR(20),
	Country VARCHAR(40)
);
