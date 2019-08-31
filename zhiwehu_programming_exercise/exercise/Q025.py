'''
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

tanawit = Person("Tanawit", "Pattanaveerangkoon")
print(tanawit.full_name) # Tanawit Pattanaveerangkoon
print(tanawit.get_full_name()) # Tanawit Pattanaveerangkoon