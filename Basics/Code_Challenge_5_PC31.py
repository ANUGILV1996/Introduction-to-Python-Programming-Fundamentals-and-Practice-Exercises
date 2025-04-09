# Code Challenge 5

# Open a text file and write some data  into it.
file = open('Fileprogram.txt', 'r')
content = file.read()
print(content)
file.close()

# Append contents.
file = open('Fileprogram.txt','a')
file.write('I am doing great.')
file.close()

# Append contents on new lines.
file = open('Fileprogram.txt','a')
file.write('Where are yoy from?\nI am from Palakkad.')
file.close()

# End of Code.
