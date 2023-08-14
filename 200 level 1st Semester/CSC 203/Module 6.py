# Page 25
radius = 1
b = radius > 0
print(b)

number = int(input("Guess a number between 1 to 5:  "))
d = number >= 4
print(d)

num = int(input("Guess a number between 1 to 5:  "))
g = num >= 4
print(g)

# Page 26
radius = 10
if radius >= 0:
    area = 3.142*radius*radius
print("The area for the circle is ", area)

# Page 26-27
number = 24
if number == 0:
    print("number is zero")
elif number < 0:
    print("number is negative")
else:
    print("number is positive")

# Page 27
age = int(input("Enter your age: "))
if 0 <= age < 18:
    print("You are a Teenager")
else:
    print("You are a Adult")

# Page 28
n = float(input("Enter a number: "))
if n < 0:
    absValue = -n
else:
    absValue = n
print(absValue)

# Page 28
n = int(input("Enter a whole number: "))
if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
# Other Solution
n = int(input("Enter a whole number: "))
print("Even Number" if n % 2 == 0 else "Odd Number")