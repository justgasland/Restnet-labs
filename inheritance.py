# adding student to school using inheritance
class Person():
    def __init__(self, age, name):
        self.age= age
        self.name= name
    
    def display(self):
        print(f"The student in the school is {self.name} and he is {self.age} years old")



class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def details(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Grade: {self.grade}"


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Students in {self.school_name}:")
        for student in self.students:
            print(student.details())


school = School("Greenwood High School")


student1 = Student("Alice", 16, "S12345", "10th Grade")
student2 = Student("Bob", 17, "S67890", "11th Grade")


school.add_student(student1)
school.add_student(student2)


school.display_students()







# Area using inheritace
class Shape:
    def area(self):
        return None 


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle is: {circle.area()}")  
print(f"area of the rectangle: {rectangle.area()}")  