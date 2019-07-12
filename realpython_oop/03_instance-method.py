class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    ## Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

mikey = Dog("Mikey", 6)

print(mikey.description()) ## Mikey is 6 years old
print(mikey.speak("Gruff Gruff")) ## Mikey says Gruff Gruff