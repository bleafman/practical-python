# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)

        headers = next(rows)

        for row in rows:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):

    prices = {}

    with open(filename, 'rt') as file:
        rows = csv.reader(file)

        for row in rows:
            if len(row) >= 2:
                stock = row[0]
                price = float(row[1])
                prices[stock] = price

    return prices
