
class MyClass:
    instance_count = 0

    def __init__(self):
      
        MyClass.instance_count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print(MyClass.get_instance_count())  
