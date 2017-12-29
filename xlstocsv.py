import csv
import xlrd

import mysql.connector

INSERT = """
    INSERT INTO transactions (
        InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
    )
    VALUES(
        %s, %s, %s, %s, FROM_UNIXTIME(%s), %s, %s, %s
    )
    """


def unfloat(cell):
    try:
        cell = int(float(cell))
    except:
        pass
    return cell


def csv_from_excel(csv_file):
    wb = xlrd.open_workbook('Online Retail.xlsx')
    print("Sheet names: %s" % wb.sheet_names())
    sh = wb.sheet_by_name('Online Retail')
    your_csv_file = open(csv_file, 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


def mysql_insert(cnx, cursor, row):
    data_txn = (
        row["InvoiceNo"],
        row["StockCode"],
        row["Description"],
        row["Quantity"],
        row["InvoiceDate"],
        row["UnitPrice"],
        row["CustomerID"],
        row["Country"]
    )

    cursor.execute(INSERT, data_txn)
    cnx.commit()


def clean_csv(csv_file):
    cnx = mysql.connector.connect(user='root', password='password', database='online_retail')
    cursor = cnx.cursor()

    out_csv_file = open('clean_' + csv_file, 'w')
    fieldnames = [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "CustomerID",
            "Country"
            ]
    wr = csv.DictWriter(f=out_csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    wr.writeheader()

    # "InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['InvoiceNo'] = unfloat(row['InvoiceNo'])
            row['StockCode'] = unfloat(row['StockCode'])
            row['Quantity'] = unfloat(row['Quantity'])
            row['CustomerID'] = unfloat(row['CustomerID'])
            row['InvoiceDate'] = int((float(row['InvoiceDate']) - 25569) * 86400)
            wr.writerow(row)
            mysql_insert(cnx, cursor, row)

    out_csv_file.close()

    cursor.close()
    cnx.close()


def main():
    csv_file = 'online_retail.csv'
    csv_from_excel(csv_file)
    clean_csv(csv_file)


main()
