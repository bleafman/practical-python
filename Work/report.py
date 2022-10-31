# report.py
#
# Exercise 2.4
import csv
from operator import itemgetter


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


def make_report(portfolio, prices):

    report = []

    for holding in portfolio:

        name, shares, price = itemgetter('name', 'shares', 'price')(holding)
        current_price = prices.get(name)

        change = current_price - price

        entry = (name, shares, price, change)

        report.append(entry)

    return report


def print_report(report=make_report(read_portfolio('Data/portfolio.csv'), read_prices('Data/prices.csv'))):

    headers = ('Name', 'Shares', 'Price', 'Change')

    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

    empty_space = ''

    print(f'{empty_space:_>10s} {empty_space:_>10s} {empty_space:_>10s} {empty_space:_>10s}')

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def total_gains(portfolio, prices):
    return current_value(portfolio, prices) - portfolio_cost(portfolio)


def portfolio_cost(portfolio):

    total_cost = 0.0

    for holding in portfolio:
        total_cost = holding['price'] * holding['shares']

    return total_cost


def current_value(portfolio, prices):

    total_value = 0.0

    for holding in portfolio:
        total_value += prices[holding['name']] * holding['shares']

    return total_value
