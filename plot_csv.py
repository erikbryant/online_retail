import csv

import matplotlib.pyplot as plt
import numpy as np


def load(start=0, count=100):
    rows = []
    i = -1

    # "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"
    with open('clean_online_retail.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            i += 1
            if i < start:
                continue
            if i > start + count:
                break
            row['Quantity'] = float(row['Quantity'])
            row['UnitPrice'] = float(row['UnitPrice'])
            if row['InvoiceNo'][0] == 'C':  # Cancellations
                continue
            if row['Quantity'] < 0:  # Damaged goods
                continue
            if row['Quantity'] > 10000:  # Outliers
                continue
            if row['UnitPrice'] < 0:
                continue
            if row['UnitPrice'] > 1000:  # Outliers
                continue
            rows.append(row)
    return rows


def main():
    rows = load(0, 1000000)

    # Generate statistics about the data we loaded.
    invoice_no = set()
    stock_code = set()
    description = set()
    quantity = set()
    customer_id = set()
    country = set()
    total_cost = 0
    for row in rows:
        # "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"
        invoice_no.add(row['InvoiceNo'])
        stock_code.add(row['StockCode'])
        description.add(row['Description'])
        quantity.add(row['Quantity'])
        customer_id.add(row['CustomerID'])
        country.add(row['Country'])
        total_cost += row['Quantity'] * row['UnitPrice']
    print("Dataset Statistics")
    print("  Rows: %d" % len(rows))
    print("  Unique InvoiceNo  : %d" % len(invoice_no))
    print("  Unique StockCode  : %d" % len(stock_code))
    print("  Unique Description: %d" % len(description))
    print("  Unique Quantity   : %d" % len(quantity))
    print("  Unique CustomerID : %d" % len(customer_id))
    print("  Unique Country    : %d" % len(country))
    print("  Items per Invoice : %.2f" % (len(rows) / len(invoice_no)))
    print("  Average Invoice $ : %.2f" % (total_cost / len(invoice_no)))

    quantity = []
    unit_price = []

    for row in rows:
        quantity.append(row['Quantity'])
        unit_price.append(row['UnitPrice'])

    q = np.array(sorted(quantity))
    print("\nNumPy")
    print("  Quantity count : %d" % len(q))
    print("           min   : %d" % q[0])
    print("           max   : %d" % q[-1])
    print("           mean  : %.2f" % q.mean())
    print("           median: %d" % q[len(q) >> 1])
    print("           std   : %.2f" % q.std())
    print("           var   : %.2f" % q.var())

    up = np.array(sorted(unit_price))
    print("\nNumPy")
    print("  UnitPrice count : %d" % len(up))
    print("            min   : %.2f" % up[0])
    print("            max   : %.2f" % up[-1])
    print("            mean  : %.2f" % up.mean())
    print("            median: %.2f" % up[len(up) >> 1])
    print("            std   : %.2f" % up.std())
    print("            var   : %.2f" % up.var())

    plt.subplot(2, 2, 1)
    plt.plot(range(len(quantity)), quantity)
    plt.ylabel("Quantity")

    plt.subplot(2, 2, 2)
    plt.plot(range(len(quantity)), sorted(quantity))
    plt.ylabel("Quantity (sorted)")

    plt.subplot(2, 2, 3)
    plt.plot(range(len(unit_price)), unit_price)
    plt.ylabel("Unit Price")

    plt.subplot(2, 2, 4)
    plt.plot(range(len(unit_price)), sorted(unit_price))
    plt.ylabel("Unit Price (sorted)")

    plt.subplots_adjust(wspace = 0.35)

    plt.show()


main()
