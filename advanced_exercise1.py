n = (input("Enter an integer: "))  # creates n and makes it hold the value of
# the user input
n = int(n)   # Converts n to an integer value from a string

for i in range(1, n + 1):  # loops from 1 to n (including n)
    print((str(i) + ' ') * i)  # prints i, an i amount of times
