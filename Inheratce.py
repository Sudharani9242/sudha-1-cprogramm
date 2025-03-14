class Animal:
  def speak(self):
    print("i'm an Animal")

class Dog(Animal):
  def speak(self):
    print("I bark")

d = Dog()   
d.speak()
