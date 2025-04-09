# Code Challenge 4

# Creating a new function.
def div(a, b):
    return a/b

#Designing the function handles zero division error.

try:
    a = int(input("enter the value of 'a':"))
    b = int(input("enter the value of 'b':"))
    print(div(a,b))

except ZeroDivisionError:
    print('Zero division error')

# End of Code.




