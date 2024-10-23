# Conversion Functions

x = 10.5 # This is a float
x = int(x) # This converts the value from a float to an integer
print(type(x))

#int(): Converts to integer
#str(): Converts to string
#float(): Converts to float (Decimal)

x = "Look! I will become the best Python programmer"
y = 10
z = 5.5

print(type(x)) # Prints the data type of x
print(type(y)) # Prints the data type of y
print(type(z)) # Prints the data type of z

print(y+z) # Prints the result of y+z - 10.5
print(type(y+z)) # Prints the variable type of y+z which is a float - 10.5
print(y+int(z)) # Prints the result of y + z when z is converted to an integer - 15
print(z+float(y)) # Prints the result of z + y when y converted to a float - 15.5
print(str(z)) # Prints the result of converting z to a string - 5
print(x + str(y) + str(z)) # Prints the result of x + y + z after converting y and z to strings
print(x + y) # We cannot add x + y here due to x being a string and y being an integer.
