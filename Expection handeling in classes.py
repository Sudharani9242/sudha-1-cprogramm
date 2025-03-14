class MyClass:
    def __init__(self):
        self.data = []
    def add_number(self, number):
        try:
            if not isinstance(number, (int, float)):
                raise ValueError("Input must be a number.")
            if not 0 <= number <= 100:
                raise ValueError("Number must be between 0 and 100.")
            
            self.data.append(number)
            print(f"Number {number} added successfully!")

        except ValueError as e:
            print(f"Error: {e}")
my_instance = MyClass()

my_instance.add_number(50)
my_instance.add_number(150)  
my_instance.add_number("Hello")  
