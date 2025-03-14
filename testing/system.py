#!/opt/homebrew/bin/python3
import sys
import os
import random

if len(sys.argv) != 2:
    sys.stderr.write("Incorrect number or args")
    sys.exit(1)

file_name = sys.argv[1]
files = os.listdir(file_name)
random.shuffle(files)

for file in files:
    print(file)