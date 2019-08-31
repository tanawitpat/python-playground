"""Question:
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass
"""

class American():
    @staticmethod
    def printNationality():
        print("America")

class NewYorker(American):
    pass

newyoker = NewYorker()
newyoker.printNationality() # America
NewYorker.printNationality() # America