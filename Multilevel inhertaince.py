# Level 1: Base class (Vehicle)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

# Level 2: Derived class (Car), inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    
    def display_car_info(self):
        self.display_info()
        print(f"Doors: {self.doors}")

# Level 3: Derived class (ElectricCar), inherits from Car
class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_size):
        super().__init__(make, model, doors)  
        self.battery_size = battery_size
    
    def display_electric_car_info(self):
        self.display_car_info()
        print(f"Battery Size: {self.battery_size} kWh")

electric_car = ElectricCar("Tesla", "Model S", 4, 100)
electric_car.display_electric_car_info()
   
   
