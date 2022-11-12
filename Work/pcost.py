# pcost.py
#
# Exercise 1.27
from os.path import exists
import csv
import sys
import report


def portfolio_cost(filename):

    if not exists(filename):
        raise RuntimeError('File does not exist')

    portfolio = report.read_portfolio(filename)

    total_cost = 0

    for holding in portfolio:
        total_cost += holding['shares'] * holding['price']

    return total_cost


# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

# cost = portfolio_cost(filename)
# print('Total Cost:', cost)
