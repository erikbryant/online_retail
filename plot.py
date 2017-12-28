import csv

import matplotlib.pyplot as plt


def plot(points):
    plt.plot(range(len(points)), points)


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
            rows.append(row)
    return rows


def main():
    rows = load(0, 1000)
    quantity = []
    unit_price = []

    for row in rows:
        quantity.append(row['Quantity'])
        unit_price.append(row['UnitPrice'])

    plot(quantity[:500])
    plot(unit_price[:500])
    plt.show()


main()
