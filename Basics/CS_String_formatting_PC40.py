# String Formatting.

# Method 1.
li = [10, 20, 30, 40]
new_string = 'my numbers:{0}, {1}, {2}, {3}'.format(li[1], li[3], li[0], li[2])
print(new_string)

# Method 2.
print("I am %s, my IDLE is %s." % ('Python', 'Pycharm'))

# For floating number.
print("I am %f, my IDLE is %s." % (3.1234, 'Pycharm'))

# For round floating number.
print("I am %3.2f, my IDLE is %s." % (3.1234, 'Pycharm'))

print("I am %3.3f, my IDLE is %s." % (3.1234, 'Pycharm'))

# For integer  number.
print("I am %d, my IDLE is %s." % (3.1234, 'Pycharm'))

# End of code.
