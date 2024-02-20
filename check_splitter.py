condition = True

def calculate_bill():
    tip_options = {
        "takeout": 10,
        "dine in": 20,
        "great service": 25
    }

    while condition == True:
        '''This loop calculates the bill amount for a group of people with try and except statements.'''
        try:
            num_people = int(input("Enter the number of guests: "))
            if num_people <= 0:
                print("The number of people must be greater than 0.")
                continue

            total_bill = float(input("Enter the total bill: "))
            if total_bill <= 0:
                print("The bill amount must be positive and greater than 0.")
                continue

            tax_rate = float(input("Enter the tax rate (as a percentage): "))
            if tax_rate < 0:
                print("The tax rate cannot be negative. Please try again.")
                continue

            print("Choose a tip option: takeout, dine in, great service")
            tip_option = input().lower()
            if tip_option not in tip_options:
                print("Invalid tip option.")
                continue

            tip_rate = tip_options[tip_option]
            break
        except ValueError:
            print("Invalid input.")

    tax = total_bill * tax_rate / 100
    tip = total_bill * tip_rate / 100
    total_bill += tax + tip

    portion = total_bill / num_people

    print(f"Each guest owes: {portion:.2f}")

calculate_bill()