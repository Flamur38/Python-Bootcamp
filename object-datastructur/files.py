
my_file = open('test.txt')
print(my_file.read())

my_file.seek(0) # Seek to the start of file (index 0)
my_file.read() # Now read it again
my_file.close() # After reading a file it's always good idea to close it.



# WRITING TO A FILE
my_file = open('test.txt', 'w+') # Anything that was in the orginal file is deleted!
my_file.write('This is a new line')
my_file.seek(0)
print(my_file.read())
my_file.close()


# APPENDING TO A FILE
my_file = open('test.txt', 'a+') # Opens the file and puts the pointer at the end
my_file.write('\nThis is being appended to test.txt')
my_file.write('\nAnd another line')
my_file.seek(0)
print(my_file.read())
my_file.close()


# Now we can use a little bit of flow to tell the program to for through every line of the file and do something:
for line in open('test.txt'):
    print(line)




