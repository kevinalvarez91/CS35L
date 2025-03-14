#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
     sys.stderr.write("Missing file name\n")
     sys.exit(1)

filename = sys.argv[1]
with open(filename, "r") as f:
     lines = f.readlines() #this is a list every element is a line

for line in lines:
    first_word = line.strip().split(" ")[0]
    print(first_word)
