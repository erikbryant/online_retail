import csv

import matplotlib.pyplot as plt

y = []
c = []
i = 0

# "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"
with open('clean_online_retail.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        i += 1
        if i > 100:
            break
        quantity = float(row['Quantity'])
        unitprice = float(row['UnitPrice'])
        if row['InvoiceNo'][0] == 'C':
            continue
        if quantity < 0:
            continue
        if quantity > 10000:
            continue
        y.append(quantity)
        c.append(quantity * unitprice)

x = range(len(y))
print("len = %s" % len(y))
plt.plot(x, y)
plt.plot(x, c)
plt.show()
