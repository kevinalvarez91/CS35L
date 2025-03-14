#!/usr/bin/python
import argparse  # Import argparse for argument parsing
import sys  # Import sys for file redirection
# when you iterate through a file, python's built in system does it line by line automatically
# with open('example.txt', 'r') as file:
#   for line in file:
#       print(line)
# this prints everything line by line 

# note repr(line), shows the exact content, of newlines and such
#i.e -> 
# 'Hello world, this is a test.\n'
# 'Python is fun!\n'
# 'Leading spaces are ignored.\n'
# 'OneWord\n'

# text = "    Hello, World!    "
# text.strip() -> Hello, World

# text = "$$$Hello$$$"
# text.strip("$") -> Hello
# text = "Hello, world! How are you?"

# text.split() -> ['Hello,', 'world!', 'How', 'are', 'you?']
# text = "apple,banana,grape"
# text.split() -> ['apple', 'banana', 'grape']

# text = "   Hello,     world!   "
# text.strip -> ['Hello', 'world!']

def main():
    parser = argparse.ArgumentParser(description="Custom cat command: Prints only the first word of each line")
    parser.add_argument("file", type=str, help="File to be displayed")

    args = parser.parse_args()

    with open(args.file, 'r') as file:
        for line in file:
            words = line.strip().split()  # Strip spaces and split into words
            if words:  # Ensure the line is not empty
                print(words[0])  # Print the first word

if __name__ == "__main__":
    main()
