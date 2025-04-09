# List-Functions
# Problem 1: Creating a list
fruits = ['apple','orange','pineapple']

# Problem 2: To add a new element.
fruits.append('cherry')
print(fruits)

# Problem 3: To add a new element in a specific position.
fruits.insert(1, 'grapes')
print(fruits)

# Problem 4: To find the number/length of elements.
print(len(fruits))

# To find the index position of an element.
print(fruits.index('cherry'))

# To remove an element.
fruits.remove('orange')
print(fruits)

# To remove an element in a specific position.
fruits.pop(1)
print(fruits)

del fruits[0]
print(fruits)

# End of code

# To delete the list
fruits.clear()
print(fruits)
