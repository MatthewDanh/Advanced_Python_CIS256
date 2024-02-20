'''
Matthew Nichols
Module 01 Programming Project: Part A
This Program: Calculates the price of ice cream based on the user's state.
'''
def main():
    state = input("In what state you drive the most: ".lower())
    price = float(input("What is the total for your ice cream: "))
    final_price = calculate_new_total(state, price)
    if state == "Rhode Island" or state == "RI":
        print("Your being charged extra for being a bad driver. Your price is: ${:.2f}".format(final_price))
    else:
        print("Your new total price is: ${:.2f}".format(final_price))

def calculate_new_total(state, price):
    '''This function calculates the new total based on the user's state.'''
    if state == "arizona" or state == "az": 
        price = (price - (price * .10))
        return price
    elif state == "colorado" or state == "co":
        price = (price - (price * .15))
        return price
    elif state == "rhode island" or state == "ri":
        price = (price + 5.00)
        return price
    else:
        return price

main()
