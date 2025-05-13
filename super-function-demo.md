### Using the super( ) function in a child class

```py
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def speak(self):
        print(f"{my_dog.name} is barking.")

my_dog = Dog("Caesar", 5, "Labrador")
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
my_dog.speak()
```