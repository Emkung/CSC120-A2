from typing import Dict, Union, Optional
from computer import*
#class provides all the necesary methods needed to add, remove, or update an resale shop's inventory 
class ResaleShop:

    # What attributes will it need?
    inventory: list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # provides the variables necessary to create the retale shop and creates a empty to append computers into 
    def __init__(self) -> None:
        self.inventory = []
    # add computer into the list 
    def buy(self, c: Computer):
        self.inventory.append(c)

    #updates on the price of the computer 
    def update_price(self, c: Computer, new_price: int):
        if c in self.inventory:
            c.price = new_price 
        else:
            print ("Item not found. Cannot update price.")
    #updates on the OS of the computer
    def update_os(self, c: Computer, new_os: int):
        if c in self.inventory:
            c.operating_system = new_os
        else:
            print ("Item not found. Cannot update OS.")
    #deletes computer from the database 
    def sell(self, c: Computer):
        self.inventory.remove(c)
    #prints out computer's identity 
    def print_inventory(self, C: Computer):
        if self.inventory:
            for C in self.inventory:
                C.printDetails()
        else:
            print("No inventory to display.")
    #indicates the value of the computer based on its  year made 
    def refurbish(self, c: Computer):
        if c in self.inventory: #locaates the computer 
            if int(c.year_made) < 2000: 
                c.price = 0
            elif int(c.year_made) < 2012:
                c.price = 250
            elif int(c.year_made) < 2018:
                c.price = 550
            else:
                c.price = 1000
        else: 
            print("item not found. Please select another item to refurbish.")
    

        


    # What methods will you need?