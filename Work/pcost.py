# pcost.py
#
# Exercise 1.27
from os.path import exists


def portfolio_cost(filename):

    if not exists(filename):
        raise RuntimeError('File does not exist')

    total_cost = 0

    with open(filename, 'rt') as file:
        headers = next(file).split(',')

        for line in file:
            row = line.split(',')

            try:
                shares = int(row[1])
            except ValueError:
                print(f'No shares were recorded for {row[0]}')
                continue

            price = float(row[2])

            total_cost = total_cost + (shares * price)

    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost)
