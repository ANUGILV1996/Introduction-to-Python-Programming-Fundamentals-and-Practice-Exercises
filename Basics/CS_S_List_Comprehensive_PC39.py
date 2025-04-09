# List Comprehensive.
result = []
for i in 'inmakes':
    result.append(i)
print(result)

# Method 2 - using list comprehension.
result = [i for i in 'inmakes']
print(result)

# To create a new list
result = ['python', 'djyango', 'flasks', 'people']
new = []
for i in result:
    if 'p' in i:
        new.append(i)
print(new)

# Method 2 - using list comprehension.
new = [i for i in result if 'p' in i]
print(new)

new1 = [i for i in range(10)]
print(new1)

# To print a list replaced by a new element (with same number of repetition in the previous list).
new3 = ['imakes' for i in result]
print(new3)

# Upper case.
new4 = [i.upper() for i in result]
print(new4)

# Multiplication.
num = [1, 4, 6, 7]
num1 = [i*i for i in num]
print(num1)

# End of code.



        

