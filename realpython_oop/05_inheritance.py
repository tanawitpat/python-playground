class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

jim = Bulldog("Jim", 12)
print(jim.description()) ## Jim is 12 years old
print(jim.run("slowly")) ## Jim runs slowly

print("Is jim an instance of Dog()? - Answer: {}".format(isinstance(jim, Dog))) 
## True

julie = Dog("Julie", 100)
print("Is julie an instance of Dog()? - Answer: {}".format(isinstance(julie, Dog)))
## True

johnnywalker = RussellTerrier("Johnny Walker", 4)
print("Is johnny walker an instance of Bulldog()? - Answer: {}".format(isinstance(johnnywalker, Bulldog)))
## False

print("Is julie and instance of jim? - Answer: {}".format(isinstance(julie, jim)))
## TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types