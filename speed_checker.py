'''
Matthew Nichols
Module 02 Lab Part B
This Program:  Calculates the time it will take to travel a distance at a certain speed.
'''
while True:
    try:
        distance = int(input("Enter the distance in miles: "))
        if distance <= 0:
            print("You must enter a number greater than 0")
            continue
        break
    except ValueError:
        print("You must enter number")
        continue
while True:
    try:
        speed = int(input("Enter your average speed traveled: "))
        if speed <= 40 or speed >= 1:
            print("You must enter a number greater than 0")
            continue
        break
    except ValueError:
        print("You must enter a number")
        continue
time = distance / speed
print("The time it will take to travel is: " + str(time))
