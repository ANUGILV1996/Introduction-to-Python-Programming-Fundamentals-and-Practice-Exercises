# Data type- Tulip.
x = (12, 13, 'hello', 'python')
print(x)

# To find the data type.
x = (12, 13, 'hello', 'python')
print(type(x))

# To access the nth element.
x = (12, 13, 'hello', 'python')
print(x[0])

# Inserting new element into Tuple: Error because of immutable.
x = (12, 13, 'hello', 'python')
x.insert(0, 'hhh')
print(x)

# Converting tuple into list.
y = list(x)
print(type(y))

# Inserting new element.
y.insert(2, 'hello1')
print(y)

# Converting list into tuple.
x = tuple(y)
print(type(x))
print(x)

# End of code.



