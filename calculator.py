# Defining a function that multiplies two numbers
def multiply(a,b):
    return a * b


# Defining a function that adds two numbers
def add(a,b):
    return a + b

# Defining a function that subtracts two numbers
def subtract(a,b):
    return a - b


# Defining a function that divides two numbers
def divide(a,b):
    return a/b

# Defining a function that squares a number
def square(a):
    return a*a

# Defining a function that cubes a number
def cube(a):
    return a*a*a  

# Defining a function that squares a number multiple times
def square_n_times (a,b):
	return a**(2*b)

print("I'm going use the calculator function to multiply 5 and 6")
x = multiply(5,6)
print(x)

print("I'm going to use the calculator function to square 4 three times")
y=square_n_times (4,3)
print(y)
