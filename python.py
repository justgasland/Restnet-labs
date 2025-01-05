# Taking user input
name = input("Enter name: ")
print(name)

# Add two numbers
a = 5
b = 3
print("Addition:", a + b) 

# Subtract two numbers
print("Subtraction:", a - b)  

# Multiply two numbers
print("Multiplication:", a * b)  

# Divide two numbers
print("Division:", a / b)  

# comparison operators in action

number = 15
print(number > 10) 

number = 10
print(number > 10) 

number = 10
# equal to
print(number == 10) 
number = 10.0
# comparing float and integer
print(number == 10) 
number = '10'
# comparing string and integer
print(number == 10) 

number = '10'
# not equal to
print(number != 10) 

number = 10
# less than or equal to
print(number <= 10) 

number = 10
# greater than or equal to
print(number >= 10) 



# Check if a number is positive or negative
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# elif
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is 0")


# while
count = 0

while count < 5:
    print(count)
    count = count + 1

#  for loop
languages = ["English", "French", "German"]

for language in languages:
    print(language)

count = 1

while count <= 5:
    print(count)
    count = count + 1
