# Page 28
batman = "Bruce Wayne"
# Length of String
print(len(batman))
# Accessing the first Character
first = batman[0]
print(first)
# Accessing the empty space in the string
space = batman[5]
print(space)
# Accessing last character
last = batman[len(batman) - 1]
print(last)


# Page 29 String Slicing
my_string = "This is My string!"
# From the start till before the 4th index
print(my_string[0:4])
print(my_string[1:7])
# From the 8th index till the end
print(my_string[8:len(my_string)])


# Page 30
# Slicing with a step
print(my_string[0:7])  # A step of 1
print(my_string[0:7:2])  # A step of 2
print(my_string[0:7:5])  # A step of 5
# Reverse Slicing
print(my_string[13:2:-1])  # Take 1 step back each time
print(my_string[17:0:-2])  # Take 2 steps back. The opposite if what happened in the slide above
# Page 31 Partial Slicing
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in the reverse (step is -1)


# Arithmetic Operators
# Addition Page 32
print(10 + 5)
float1 = 13.65
float2 = 3.40
print(float1 + float2)
num1 = 20
fit1 = 10.5
print(num1 + fit1)

# Subtraction
print(10-5)
float3 = -18.678
float4 = 3.55
print(float3 - float4)
num2 = 20
fit2 = 10.5
print(num2 - fit2)

# Multiplication
print(40 * 10)
float5 = 5.5
float6 = 4.5
print(float5 * float6)
print(10.2 * 3)

# Division
print(40 / 10)
print(float5 / float6)
print(12.4 / 2)

# Modulo
print(43 // 10)
print(float5 // float6)
print(12.4 // 2)

# Precedence
print(10 - 3 * 2)  # Different Precedence
# Same Precedence
print(3 * 20 / 5)  # Multiplication computed first, followed by Division
print(3 / 20 * 5)  # Division computed first, followed by Multiplication

# Parentheses
print((10 - 3) * 2)  # Subtraction occurs first
print((18 + 2) / (10 % 8))


# Comparison Operators
num3 = 5
num4 = 10
num5 = 10
print(num4 > num3)  # 10 is greater than 5
print(num3 > num4)  # 5 is not greater than 10
print(num4 is num5)  # Both have the same value
print(num5 is not num3)  # Both have different values
print(3 + 10 == 5 + 5)  # Both are not Equal
print(3 <= 2)  # 3 is not less than or equal to 2


# Assignment Operators
# Page 37 Assigning Values
year = 2019
print(year)
year = 2020
print(year)
year = year + 1  # Using the existing value to create a new one
print(year)

first2 = 20
second2 = first2
first2 = 35  # Updating 'first2'
print(first2, second2)  # 'second' remains unchanged
# Page 38
num6 = 10
print(num6)
num6 += 5
print(num6)
num6 -= 5
print(num6)
num6 *= 2
print(num6)
num6 /= 2
print(num6)
num6 **= 2
print(num6)

# Logical Operators
# OR Expression
my_bool = True or False
print(my_bool)
# AND Expression
my_bool = True and False
print(my_bool)
# NOT Expression
my_bool = False
print(not my_bool)

# BitWise Operators
num7 = 10  # Binary value = 01010
num8 = 20  # Binary value = 10100
print(num7 & num8)  # 00000
print(num7 | num8)  # 11110
print(num7 ^ num8)  # 11110
print(~num7)  # 1111 0101
print(num7 << 3)  # 0101 0000
print(num7 >> 3)  # 0010


# String Data Type
# Comparison Operators
print('a' < 'b')  # 'a' has a smaller Unicode Value
house = "Gryffindor"
house_copy = "Gryffindor"
print(house == house_copy)
new_house = "Slytherin"
print(house == new_house)
print(new_house <= house)
print(new_house >= house)

# Concatenation
first_half = "Bat"
second_half = "Man"
# Using + Operator
full_name = first_half + second_half
print(full_name)
# Using * Operator
print("ha" * 3)

# Search
random_string = "This is a random string"
print('of' in random_string)  # Check wheather 'of' exists in random_string
print('random' in random_string)  # 'random' exists!

# Making List
my_list = [1, 2.5, "A String", True]
print(my_list)
print(my_list[2])
print(len(my_list))