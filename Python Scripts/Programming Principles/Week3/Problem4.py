"""
// Salary + Commission calculator //
"""

# Inputs
base_wage = 36.25
car_commission = 0
overtime = 0
hours_worked = int(input('How many hours were worked? '))
cars_sold = int(input('Total number of cars sold for the week? '))

# Car Commission
if cars_sold > 5:
    car_commission = (cars_sold - 5) * 200
elif cars_sold <= 5:
    car_commission = 0

# Any Overtime + Final Pay
if hours_worked > 37:
    overtime = (hours_worked - 37) * (base_wage * 1.5)
    print('The salary is:', (base_wage * 37) + overtime + car_commission)
elif hours_worked <= 37:
    overtime = 0
    print('The salary is:', (base_wage * hours_worked) + car_commission)
