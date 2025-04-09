# Additional Code Challenge

# Question 1
my_list = ['Apple', 'Orange', 'Pineapple', 'Strawberry', 'Grapes']

new_list = ['I like {0}, {1}, {2}, {3}'.format(my_list[3], my_list[2], my_list[0], my_list[1])]
print(new_list)

# Question 2
list_1 = [66, 234, 546, 2453, 982, 123, 965, 333]
print(list_1[2:7])

# Question 3

my_tuple = (9, 12, 28, 24, 36, 42, 66)
list_tup = list(my_tuple)
list_tup.insert(0, 3)
list_tup.append(99)
my_tuple = tuple(list_tup)
print(my_tuple)
print(my_tuple[7])

# End of code.
