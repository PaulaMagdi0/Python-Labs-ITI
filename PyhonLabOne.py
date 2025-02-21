# Question 1
a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print(a)

# Question 2
a = [10, 20, 30, 20, 40, 50]
val = a.pop(1)
print("value:", val)
print(a)

# Question 3
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]
print(a)

# Question 4
a = [10, 20, 30, 40, 50, 60, 70]
del a[:]
print(a)

# Question 5
string = input("Enter a string: ")
count = string.count('iti')
print(f"{count=}")

# Question 6
while True:
    binary = input("Enter your binary number: ")
    if all(char in '01' for char in binary):
        decimal = int(binary, 2)
        print("Decimal Number:", decimal)
        break
    else:
        print("Please enter a binary number (only 0s and 1s): ")

# Question 7
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Not Fizz or Buzz"

num = int(input("Enter a number: "))
print(fizzbuzz(num))

# Question 8
import math
radius = float(input("Enter the radius: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("Area: ", area)
print("Circumference: ", circumference)

# Question 9
import re

while True:
    name = input("Enter your name: ")
    if name.strip() and not name.isdigit():
        break
    print("Invalid name. Please enter a valid name.")

while True:
    email = input("Enter your email: ")
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        break
    print("Invalid email. Please enter a valid email address.")

print("Name: ", name)
print("Email: ", email)
