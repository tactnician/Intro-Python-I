"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# f = open('foo.txt', 'r')
# read_data = f.read()
# print(read_data)
# f.close()
# f.closed

with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)

f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as f:
    f.write(' Line 1\n Line 2 \n Line 3')

with open('bar.txt') as f: 
    read_data = f.read()
    print(read_data)