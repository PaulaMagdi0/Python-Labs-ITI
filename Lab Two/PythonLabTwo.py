# Question 1:
def calculator(operation, a, b):
    match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divided":
            return a / b if b != 0 else "Cannot divided by zero"
        case _:
            return "Invalid operation"

operation = "add"
a, b = 20, 2
print(calculator(operation, a, b))

# Question 2:
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
filtered_numbers = [num for num in numbers if num % 2 != 0]

print(filtered_numbers)
print("Count =", len(filtered_numbers))

# Question 3:
def is_valid_password(password):
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password)):
        return "Valid Password"
    return "Invalid Password"

password = "Password1020"
print(is_valid_password(password))

# Question 4: 
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)

# Question 5: 
def longest_alphabetical_substring(s):
    longest = current = s[0]

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]: 
            current += s[i]
            if len(current) > len(longest):
                longest = current
        else:
            current = s[i]

    return longest

s = "PaulaMagdy"
print("The longest substring in alphabetical order is:", longest_alphabetical_substring(s))

# Question 6: 
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return "Valid Email" if re.match(pattern, email) else "Invalid Email"

email = "paula@gmail.com"
print(is_valid_email(email))
