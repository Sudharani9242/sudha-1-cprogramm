
marks = float(input("Enter the student's marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"
print(f"The student's grade is: {grade}")
