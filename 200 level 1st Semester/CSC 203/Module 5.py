# String Concatenation
print("Hello, "+"World")
print(int(3+2))
print(int(4.0/2))
print(int(5/2))
print(5/2)
print(2**2)
print(4%2)

# Find the area of a circle
radius = int(input('Enter the radius of a circle: '))
area = 3.142 * radius**2
print("The area of a circle of Radius " ,radius, " is ",area)

k = 5
g = str(k)
print("k",type(k))
print("g",type(g))

T = int(input('Enter a number: '))
p = str(T)
print("T",type(T))
print("p",type(p))

q = "10"
r = int(q)
print("q",type(q))
print("r",type(r))

c = 10.6
d = int(c)
print(d)

a = 10.6
b = round(a)
print(b)

x1 = int(input("Enter point1 separated with comma: "))
x2 = int(input("Enter point1 separated with comma: "))
y1 = int(input("Enter point2 separated with comma: "))
y2 = int(input("Enter point1 separated with comma: "))
x3 = x2 - x1
y3 = y2 - y1
distance = ((((x3)**2)+((y3)**2))**0.5)
print(distance)