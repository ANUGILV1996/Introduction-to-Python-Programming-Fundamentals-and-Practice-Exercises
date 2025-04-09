# For Loop - Part 3

# Problem 1:
for i in range(1, 5):
    print(i)

# Problem 2: To print in a single line
for i in range(1, 5):
    print(i, end='')

# Problem 3: To print in a single line with a space/comma or symbol between the numbers
for i in range(1, 5):
    print(i, end=',')

# Problem 4: To print the numbers in new line
for i in range(1, 5):
    print(i, end='\n')

# Nested for loop
# Problem 5: To print the numbers 3 times in 3 lines
for x in range(3):
    for i in range(1, 5):
        print(i, end=' ')
    print()

# Problem 6: To print in patterns
for x in range(4):
    for j in range(x+1):
        print('*', end=' ')
    print()

# Problem 7: To print cross product
x = [22, 23]
y = [67, 89]
for i in x:
    for j in y:
        print(i, j)

# End of code.