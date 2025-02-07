# report.py
#
# Exercise 2.4
import csv
from operator import itemgetter
import fileparse


def read_portfolio(filename):
    with open(filename) as file:
        return fileparse.parse_file(file, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    with open(filename) as file:
        return fileparse.parse_file(file, types=[str, float], has_headers=False)

def make_report(portfolio, prices):

    report = []

    prices_dict = dict(prices)

    for holding in portfolio:

        name, shares, price = itemgetter('name', 'shares', 'price')(holding)
        current_price = prices_dict.get(name)

        change = current_price - price

        entry = (name, shares, price, change)

        report.append(entry)

    return report


def print_report(report):

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

def main(argv):
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfoliofile pricefile')

    portfolio = read_portfolio(argv[1])
    prices = read_prices(argv[2])

    report = make_report(portfolio, prices)
    print_report(report)

if __name__ == '__main__':
    import sys
    main(sys.argv)