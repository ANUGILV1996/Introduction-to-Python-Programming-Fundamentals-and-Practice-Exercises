# File Handling

# Problem 1: create a new file.
file = open('demo.txt','w')
file.close()

# Problem 2: read the file
file = open('demo.txt','r')
content = file.read()
print(content)
file.close()

#Problem 3: Read line.
file = open('demo.txt','r')
content = file.readline()
print(content)
file.close()

# Problem 4: Setting parameter.
file = open('demo.txt','r')
content = file.read(10)
print(content)
file.close()

#Problem 5: Write contents.
file = open('demo.txt','w')
file.write('am python djyango')
file.close()

#Problem 6: append contents.
file = open('demo.txt','a')
file.write(' am append')
file.close()

# End of Code.




