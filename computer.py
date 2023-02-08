from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
# allows the creation of a "computer" that would later be stored into inventory 
class Computer:

    # What attributes will it need?
    description: str = ""
    processor_type: str = ""
    hard_drive_copacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # provide the variables necesary to create a computer
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_copacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # method prints out specific information regarding the computer 
    def printDetails(self):
        print(self.description)
        print(self.processor_type) 
        print(self.hard_drive_copacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)


    # What methods will you need?