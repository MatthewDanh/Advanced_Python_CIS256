'''
Matthew Nichols
Module 01 Programming Project: Part B
This Program: Sets up a class for a cooler in the breakroom.
'''

class Cooler:
    '''This creates a class for the water cooler in the breakroom.'''
    def __init__(self, location, water):
        '''This is the constructor for the class Breakroom.'''
        self.location = location
        self.water = water
    
    def refill(self):
        '''This is the method for when the cooler is refilled.'''
        if self.water < 5:
            self.water = 20
        return self.water
    
    def pour(self):
        '''This is the method for when an employee pours water from the cooler.'''
        if self.water < 0.5:
            print("Out of water!")
        elif self.water <= 5:
            print("Water is low")
        else:
            self.water -= 0.5
        return self.water
    
    def move(self, location):
        '''This is the method for if the cooler is moved to a different location.'''
        self.location = location
        return self.location

breakroom_cooler = Cooler('breakroom', 20)
lobby_cooler = Cooler('Lobby', 5)
warehouse_cooler = Cooler('Warehouse', 0)

breakroom_cooler.pour()
lobby_cooler.pour()
warehouse_cooler.pour()

print(breakroom_cooler.location, breakroom_cooler.water)
print(lobby_cooler.location, lobby_cooler.water)
print(warehouse_cooler.location, warehouse_cooler.water)

warehouse_cooler.move('office')
warehouse_cooler.refill()

print(warehouse_cooler.location, warehouse_cooler.water)
