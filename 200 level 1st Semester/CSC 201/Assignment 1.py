# Question 2
my_string = "0123456789"
print(my_string[-2:-6:-2])

# Question 3
x = 20
y = 5

result = (x + True)/(4-y * False)
print(result)


# Question 8
str = 'Hello World!'
print(str[0])

# Question B Create a program that reads three integers from the user and displays them in sorted order (from
# smallest to largest). Use the min and max functions to find the smallest and largest values. The middle value can
# be found by computing the sum of all three values, and then subtracting the minimum value and the maximum value.

# Read integers from user
# Read three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Find the smallest and largest values
min_val = min(num1, num2, num3)
max_val = max(num1, num2, num3)

# Find the middle value
middle_val = sum([num1, num2, num3]) - min_val - max_val

# Display the sorted values
print("Sorted values:", min_val, middle_val, max_val)