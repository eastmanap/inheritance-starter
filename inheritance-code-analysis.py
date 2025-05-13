class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{animal1.name.title()} is making a sound no one has heard before.")
        print(f"Maybe {animal1.name.title()} feels threatened...")

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{my_dog.name} is barking at the UPS driver.")

my_dog = Dog("Gladiator", 5, "German Shepherd")
print(f"My dog's name is {my_dog.name.title()}.\n")
print(f"{my_dog.name.title()} is {my_dog.age} years old.\n")
print(f"{my_dog.name.title()} is a {my_dog.breed}.\n")
my_dog.speak()
print()
animal1 = Animal("Simon", 1.5)
animal1.speak()
print(f"\n{animal1.name.title()} is {animal1.age} years old.")