import os, sys

# Take user input and open directory
path = input('What Path? ')
dirs = os.listdir(path)

# Print all files and Directories
for file in dirs:
    print(file)
