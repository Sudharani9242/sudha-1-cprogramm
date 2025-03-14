
class Vehicle:
  def __init__(self,name,model):
    self.name=name
    self.model=model
  def info(self):
    print(f"Name: {self.name}\nModel: {self.model}")
class Car(Vehicle):
  def __init__(self,name,model,color):
    super().__init__(name,model)
    self.color=color
  def info(self):
    super().info()
    print(f"Color: {self.color}")
car=Car("rolls royce","2023","red")
car.info()
