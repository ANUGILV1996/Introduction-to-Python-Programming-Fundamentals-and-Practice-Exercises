# Functional Programming

def addition(a, b):
    return a + b


def square(c):
    return c * c


x = int(input('Number a:'))
y = int(input('Number b:'))

result = square(addition(x, y))
print('result =', result)

# End of Code.
