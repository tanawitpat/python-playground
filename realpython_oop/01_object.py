class Dog:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age

philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

print("{} is {}".format(philo.name, philo.age))
print("{} is a {}!".format(philo.name, philo.species))
print("{} is {}".format(mikey.name, mikey.age))
print("{} is a {}!".format(mikey.name, mikey.species))