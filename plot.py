import csv

import matplotlib.pyplot as plt

# "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"
with open('online_retail.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['InvoiceNo'] = int(float(row['InvoiceNo']))

for r in range(10):
    print(row[r]['InvoiceNo'])

plt.plot(x, y)

plt.show()