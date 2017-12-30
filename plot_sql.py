import matplotlib.pyplot as plt
import mysql.connector
import numpy as np


def sql_query(query=""):
    results = None

    cnx = mysql.connector.connect(user='root', password='password', database='online_retail')
    cursor = cnx.cursor()
    for result in cursor.execute(query, multi=True):
        if result.with_rows:
            if results:
                raise ValueError
            results = result.fetchall()
            print("Rows produced by statement '{}': {}".format(
                result.statement, len(results)))
            # print(results)
        else:
            print("Number of rows affected by statement '{}': {}".format(
                result.statement, result.rowcount))
    cnx.commit()
    cursor.close()
    cnx.close()

    return results


def flip(results):
    #
    # results is in the form:
    # [(col1, col2), (col1, col2), ...]
    # [(6, 2.55), (6, 3.39), (8, 2.75), (6, 3.39), (6, 3.39)]
    #
    # But, to plot the data we need it in the form:
    # col1 = [6, 6, 8, 6, 6]
    # col2 = [2.55, 3.39, 2.75, 3.39, 3.39]
    #
    plot_data = []
    cols = len(results[0])
    for i in range(cols):
        temp = []
        for j in range(len(results)):
            temp.append(results[j][i])
        plot_data.append(temp)

    return plot_data


def print_stats(array, title):
    print("%s Statistics" % title)
    print("  count : %d" % len(array))
    print("  min   : %s" % array[0])
    print("  max   : %s" % array[-1])
    print("  median: %s" % array[len(array) >> 1])
    print("  mean  : %.2f" % array.mean())
    print("  std   : %.2f" % array.std())
    print("  var   : %.2f" % array.var())


def main():
    labels = [
        "Quantity",
        "UnitPrice",
        "Quantity * UnitPrice"
    ]

    query = """
        SELECT %s FROM transactions where customerid != '' and stockcode != 'POST' LIMIT 100
        """ % (", ".join(labels))
    results = sql_query(query)
    plot_data = flip(results)
    datasets = len(labels)

    for i in range(datasets):
        data = np.array(plot_data[i])

        print_stats(data, labels[i])

        plt.subplot(datasets, 2, (i*2)+1)
        plt.plot(range(len(data)), data)
        plt.ylabel(labels[i])

        plt.subplot(datasets, 2, (i*2)+2)
        plt.plot(range(len(data)), sorted(data))
        plt.ylabel("%s (sorted)" % labels[i])

    plt.show()


main()
