
class Animal:
    def move(self):
        pass  
class Bird(Animal):
    def move(self):
        print("The bird flies in the sky.")
class Fish(Animal):
    def move(self):
        print("The fish swims in the water.")
def animal_move(animal):
    animal.move()  
bird = Bird()
fish = Fish()
animal_move(bird)  
animal_move(fish)  
