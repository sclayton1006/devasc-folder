#Python3.8

""" This small program opens the local textfile.txt and reads the contents
The contants are printed to the screen when you run the print command"""

readdata = open("textfile.txt", "r")  # Open the file in python, but open only
print(readdata.read())                # Read the data of the file and print
readdata.close()                      # Close the file to prevent open file lock
print("\n\n============================================================")

""" An alternative to this is to provide the commands as a context manager
or a 'with statement'"""

with open("textfile.txt", "r") as data:
    print(f"This output is from the context manager \n{data.read()}")
print("\n\n============================================================")

""" You can add data to a file too by adding the 'a+' (a = append to the end of
the file if it exists and + = open for updating (reading and writing)) as the
second argument in place of the 'r' that denotes 'read' and is the default """

# NOTE - you don't have to state the "r" argument as it is the default argument.
# You can simply state:
# "with open("txtfile.txt") as data:" if you want to read only. No 'r' required.

with open("textfile.txt", "a+") as data:
    data.write("I added this onto the end of the file")

# Writing data into the file can be done with the above two lines but the same
# line cannot be used to print the file. It didn't work for me anyway. I had
# to re-open the file with the default "r" argument.

print("Then we can add some more information onto the file with the 'a+' \
argument\n\n")
with open("textfile.txt") as data:
    print(data.read())
