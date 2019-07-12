class Dog:
    species = "mammal"

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = "reptile"

frank = SomeBreed()
print(frank.species) ## mammal

beans = SomeOtherBreed()
print(beans.species) ## reptile