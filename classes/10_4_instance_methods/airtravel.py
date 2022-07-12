#Core Python 3.6: Getting Started | Classes | Defining Classes

"""Model for aircraft flights"""
class Flight:
    #Instance methods must accept a reference to the actual instance on which the...
    #...method was called as the first arguement.
    def number(self):
        return "SN060"
#Defining f and using different ways of accessing the same data/value
f = Flight()
print(f.number())
print(Flight.number(f))