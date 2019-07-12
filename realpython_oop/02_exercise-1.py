class Person:
    species = "human"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Oui = Person("Oui", 23)
Mom = Person("Mom", 56)
Dad = Person("Dad", 60)

def get_biggest_number(*args):
    return max(args)

print("The oldest person is {} years old".format(get_biggest_number(Oui.age, Mom.age, Dad.age)))