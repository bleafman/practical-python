# pcost.py
#
# Exercise 1.27
from os.path import exists
import csv
import sys


def portfolio_cost(filename):

    if not exists(filename):
        raise RuntimeError('File does not exist')

    total_cost = 0

    with open(filename, 'rt') as file:

        rows = csv.reader(file)

        headers = next(rows)

        for row in rows:

            try:
                shares = int(row[1])
            except ValueError:
                print(f'No shares were recorded for {row[0]}')
                continue

            price = float(row[2])

            total_cost = total_cost + (shares * price)

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost:', cost)
