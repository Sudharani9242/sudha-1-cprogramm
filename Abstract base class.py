
from abc import ABC, abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius
circle = Circle(5)
print(f"The area of the circle is: {circle.area()}")

  

