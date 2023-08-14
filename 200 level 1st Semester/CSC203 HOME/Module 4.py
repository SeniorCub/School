# Page 14
name = input("Enter Your Name: ")
print("Your name is: ", name)
print("Type of variable 'name' is: ", type(name)),

# Page 14
# Input function to read numbers and expressions
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
print(number1 + number2)
print("Type of variable 'number1' is: ", type(number1)),

# Page 14
# Compute a circle's circumference to read radius
# Declare radius variable and read value from user
radius = int(input("Enter the circle's radius: "))
# compute circumference using the formula
circumference = 2 * 3.14159 * radius
# print the result on the screen
print("Circumference for the circle of radius", radius, "is", circumference),

# Page 15
# Prompt the user to enter three numbers
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))
# compute average
average = (number1 + number2 + number3) / 3
# Dispaly result
print("The average of", number1, number2, number3, "is: ", average),

# Page 15
# Prompt the user to enter three numbers
[number1, number2, number3] = input("Enter three numbers separated by commas: ")
# compute average
average = (number1 + number2 + number3) / 3
# Dispaly result
print("The average of", number1, number2, number3, "is: ", average)
