# Exception Handling.

# Problem 1:
a = 4
b = 0
print(a/b)

# Problem 2: Using 'try' and 'except' block.
try:
    a = 4
    b = 0
    print(a / b)
except:
    print('there is a division error')

# Problem 3: Using 'try' and 'except' block.
try:
    a = 4
    b = 2
    print(a / b)
except:
    print('there is a division error')

# Problem 4: Using 'try', 'except' and 'finally' block.
try:
    a = 4
    b = 2
    print(a / b)
except:
    print('there is a division error')
finally:
    print('am finally')

# Problem 5: Index error.
try:
    a = [12, 34, 56, 78]
    print(a[4])
except:
    print('there is an index error')
finally:
    print('am finally')

# Problem 6: Type error.
try:
    q = 8
    w = "xyz"
    print(q+w)

except TypeError:
    print("Can not add int and string")

#Problem 7: Index Error.
try:
    q = [2,3,4]
    w = 9
    print(q[6])
except IndexError:
    print ("out of range")


# Problem 8: Name error.
def sample(x,y):
    sum(x+y)
    return sum
a = 10
b = 12
sample(a, u)

# Problem 9: Attribute error.
sample = 'hai'
sample.reverese

# End of Code.











