'''
Matthew Nichols
Module 02 Lab Part A
This Program: Calculates the paycheck amount for an employee.  
'''
while True:
    '''This loop calculates the paycheck amount for an employee with try and except statements.'''
    try:
        hours = int(input("Enter hours worked for the week: "))
        rate = int(input("Enter pay rate per hour: "))
        break
    except ValueError:
        print("Please enter a number")
        continue
paycheck = hours * rate
print("Your total paycheck is: " + str(paycheck))

paycheck_tax = paycheck * .30
print("Your tax is: " + str(paycheck_tax))

paycheck_net = paycheck - paycheck_tax
print("Your total paycheck after tax is: " + str(paycheck_net))
