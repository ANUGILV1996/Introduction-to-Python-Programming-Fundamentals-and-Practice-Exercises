# Some more type-Dictionary
x = {'chair': 500,
     'table': 300,
     34: 'python'}
print(x)

# Using some duplication. What will happen?
x = {'chair': 500,
     'table': 300,
     'chair': 'Python'}
print(x)

# Printing vales using key.
x = {'chair': 500,
     'table': 300,
     34: 'python'}
print(x['chair'])

# To find the length.
x = {'chair': 500,
     'table': 300,
     34: 'python'}
print(len(x))

# To add new key and value.
x['vegetable'] = 120
print(x)

# or.
x.update({12: 'django'})
print(x)

# To delete key and value.
x.pop('table')
print(x)

# To see the keys using For loop.
for i in x:
    print(i)
# Or
for i in x.keys():
    print(i)

# To see the values using For loop.
for i in x.values():
    print(i)

# To see the keys and values using For loop.
for i in x.items():
    print(i)

# End of Code
