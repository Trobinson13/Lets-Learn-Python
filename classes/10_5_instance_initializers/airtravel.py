#Core Python 3.6: Getting Started | Classes | Defining Classes

"""Model for aircraft flights"""
class Flight:
    
    #The first arguement to dunder init must be self
    #__init__ is an initializer, not a constructor
    def __init__(self, number):
        #_number avoids "name clash" of method with the same name
        #By convention, implementation details start with underscore
        self._number = number

    def number(self):
        return "SN060"

