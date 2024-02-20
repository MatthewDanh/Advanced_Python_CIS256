'''
Matthew Nichols
Module 01 Lab 
This Program: Stores the names of the user's current Best/Least favorite friends.  
'''
# Ask the user to input the amount of freinds and store in a variable:
num_friends = int(input("Enter a number: "))
friends = []

# Loop through list and enter name:
for i in range(num_friends):
    friend = input("Enter a name: ")
    friends.append(friend)

# Print the name of the user's best/least/entire list friend:
    print("Your Best Friend is {}" + friends[0])  
    print("Your Least Friend is {}" + friends[-1])
    # note: originally i didn't havethe {} but stupid google put a AI generating thing on the seach results. 
    # It said this was better, but just wanted to note this. I turned it off for future.

# Create a loop to print out the entire list of friends:
    for friend in friends:
        print(friend)       

# Initialize variable with empty string in it:
    acronym = " ".join(people[0] for people in friends)
    print("/n The first letter in each name would spell: " + acronym)

'''
Refernces: 
    1. https://realpython.com/python-strings/ 
    2. https://peps.python.org/pep-0008/#programming-recommendations
    3. https://www.w3schools.com/python/python_datatypes.asp
'''