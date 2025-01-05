
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
print("Division:", a / b)  


# # Check if a number is positive or negative
# number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")







# OOP


# Making the plan (class)
class ToyCar:
    def __init__(self, color):  # This is like choosing the toy's color
        self.color = color

    def go_vroom(self):  # This is what the car can do
        print("Vroom vroom!")

# Making the actual toy (object)
my_car = ToyCar("red")

# Playing with the toy
print(f"My car is {my_car.color}.")  # Checking its color
my_car.go_vroom()  # Making it go vroom


class mystudent:
    def __init__(self,name, age):
        self.name= name
        self.age =age
    
    def marks(self):
        print(' your score is ')
    
    def ages(self):
        print(' your age is ')

age= mystudent.ages(12)
mark= mystudent.marks(32)

print(f"{age}")
print(f"{mark}")