# mortgage.py
#
# Exercise 1.7

# User variables

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

####

principle = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0

while principle > 0:
    if (extra_payment_start_month <= current_month and current_month <= extra_payment_end_month):
        principle = (principle * (1 + rate/12)) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principle = principle * (1 + rate/12) - payment
        total_paid = total_paid + payment

    current_month += 1

    if (principle < 0):
        refund = abs(principle)
        total_paid = total_paid - refund
        principle = 0

    # print(round(current_month, 2), round(total_paid, 2), round(principle, 2))

print(f'Total paid: ${total_paid:0.2f}')
print('Total months:', current_month)
