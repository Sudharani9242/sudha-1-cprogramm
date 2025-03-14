
class MyClass:
    class_variable = 10
    
    def __init__(self, value):
        self.value = value
    def instance_method(self):
        print(f"Instance method called. Value: {self.value}")
    @classmethod
    def class_method(cls):
        print(f"Class method called. Class variable: {cls.class_variable}")
    
    @staticmethod
    def static_method(value):
        print(f"Static method called with value: {value}")
      
obj = MyClass(20)
obj.instance_method()  
MyClass.class_method()  
MyClass.static_method(100)  
obj.static_method(200)  
