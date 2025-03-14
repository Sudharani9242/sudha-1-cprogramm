
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        return f"{self.name} makes a sound."
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    def bark(self):
        return f"{self.name} barks: Woof! Woof!"
dog = Dog(name="Rex", breed="Golden Retriever")
print(dog.speak())  
print(dog.bark())   
