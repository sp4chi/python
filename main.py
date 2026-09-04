from car import Car
from student import Student

car = Car("Posche", 2026, "Yellow", True)
car_1 = Car("Mustang", 2026, "Blue", True)
car_2 = Car("Byd", 2025, "Grey", False)
car.drive()
car.stop()
car_1.drive()
car_2.stop()

student = Student("Patrick", 10)
student_1 = Student("Sponge bob", 15)
print(student.name,student_1.name)
print(student.age,student_1.age)
print(student.class_year, student_1.class_year, Student.class_year)
student_2 = Student("Rose",66)
student_3 = Student("Raj",18)
print(Student.num_student)
