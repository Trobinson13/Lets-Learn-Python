#Core Python 3.6: Getting Started | Classes | Defining Classes

"""Model for aircraft flights"""
from xml.dom import ValidationErr


class Flight:
    
    #The first arguement to dunder init must be self
    #__init__ is an initializer, not a constructor
    def __init__(self, number):
        #Class Invariants.
        #Validating that the first two characters of number are letters
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        #_number avoids "name clash" of method with the same name
        #By convention, implementation details start with underscore
        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

f = Flight("SN060")
print(f.number())
print(f._number)
print(f.airline())

