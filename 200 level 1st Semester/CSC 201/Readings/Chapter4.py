def my_print_function(): # No Parameter
    print("This")
    print("is")
    print("A")
    print("function")
# Function ended
# calling the function in the program  multiple times
my_print_function()
my_print_function()

def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)
num1 = 10
num2 = 20
minimum(num1 , num2)

name = "Ned"
def func():
    name = "Stark"
func()
print(name)  # accessing 'name' outside the function

num = 20
def multipy_by_10(n):
    n *= 10
    num = n  # Changing the value inside the function
    print("Value of num inside the function is", num)
    return n

multipy_by_10(num)
print("Value of num outside the function is", num)