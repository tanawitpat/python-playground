class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return self.name, self.age

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "%s is walking!" % (self.name)

class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)

my_pets.walk()