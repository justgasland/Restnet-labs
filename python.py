
# # Taking user input
# name = input("Enter name: ")
# print(name)

# # Add two numbers
# a = 5
# b = 3
# print("Addition:", a + b) 

# # Subtract two numbers
# print("Subtraction:", a - b)  

# # Multiply two numbers
# print("Multiplication:", a * b)  

# Divide two numbers
# print("Division:", a / b)  


# # # Check if a number is positive or negative
# # number = int(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative.")







# OOP


# # Making the plan (class)
# class ToyCar:
#     def __init__(self, color):  # This is like choosing the toy's color
#         self.color = color

#     def go_vroom(self):  # This is what the car can do
#         print("Vroom vroom!")

# # Making the actual toy (object)
# my_car = ToyCar("red")

# # Playing with the toy
# print(f"My car is {my_car.color}.")  # Checking its color
# my_car.go_vroom()  # Making it go vroom


# class mystudent:
#     def __init__(self,name, age):
#         self.name= name
#         self.age =age
    
#     def marks(self):
#         print(' your score is ')
    
#     def ages(self):
#         print(' your age is ')

# age= mystudent.ages(12)
# mark= mystudent.marks(32)

# print(f"{age}")
# print(f"{mark}")

# class student():
#     def __init__(self, brand, power_rating):
#         self.brand=  brand
#         self.power_rating= power_rating
# smeg= student(brand='smeg', power_rating='20')
# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

# class car():
#     def __init__(self, sound, color) :
#         self.color= color
#         self.sound= sound
# mycar=car(sound='vroom', color='red')
# print(mycar.color)
# print(mycar.sound)


# class Student:
#     def check_pass_fail(self):
#         if self.marks >= 40:
#             return True
#         else:
#             return False

# student1 = Student()
# student1.name = "Harry"
# student1.marks = 85

# did_pass = student1.check_pass_fail()
# print(did_pass)

# student2 = Student()
# student2.name = "Janet"
# student2.marks = 30
# did_pass = student2.check_pass_fail()
# print(did_pass)



# Computing area of circle, rectangle and square,

class  area:
    def __init__(self,r, b, l, ):
        self.r=r
        self.b= b
        self.l=l
    
    def square(self):
        sqr= self.l*self.l
        print('the area of the sqaure is ', sqr)
    def circle(self):
        cir = 3.142 * self.r * self.r
        print('the area of the circle is ', cir)
    def rectangle(self):
        rec = self.b* self.l
        print('tha area of the rectangle is ', rec)

math= area(3, 4,6)
math.circle()
math.rectangle()
math.square()


# School portal
class Student:
    def __init__(self, name, age, level, course, email, grade):
        self.name = name
        self.age = age
        self.level = level
        self.course = course
        self.email = email
        self.grade = grade

    def display_student(self):
        return f"Name= {self.name}, Age= {self.age}, Email= {self.email}, Course= {self.course}, Level= {self.level}, Grade= {self.grade}"

class School:
    def __init__(self):
        self.students = []  
    
    def add_student(self, name, age, email, course, level, grade):
        student = Student(name, age, level, course, email, grade)  
        self.students.append(student)
        print("Student added successfully.")
        print(student.display_student()) 

my_school = School()
my_school.add_student("Alice", 12, 'alice@gmail.com', 'Computer Science', '300lvl', 32)
my_school.add_student("Bob", 14, 'bob@gmail.com', 'Accounting', '200lvl', 35)
