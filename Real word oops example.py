
class Student:
    def __init__(self, name, age, marks):
        self.name = name        
        self.age = age          
        self.marks = marks      

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"  
        elif self.marks >= 80:
            return "A"   
        elif self.marks >= 70:
            return "B"   
        elif self.marks >= 60:
            return "C" 
        elif self.marks >= 50:
            return "D"   
        else:
            return "F"   
student_1 = Student("ram", 16, 85)
print(f"Student: {student_1.name}, Age: {student_1.age}, Marks: {student_1.marks}, Grade: {student_1.calculate_grade()}")
