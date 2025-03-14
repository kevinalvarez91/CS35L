#!/usr/bin/python
import random
import argparse
import os

def main():
    # Argument Parser Setup
    parser = argparse.ArgumentParser(description="Custom ls")
    parser.add_argument("directory", type=str, help="Path to be displayed")

    args = parser.parse_args()

    # Get list of files in the specified directory
    dir_list = os.listdir(args.directory)

    # Shuffle the list of filenames
    random.shuffle(dir_list)

    # Print shuffled file names (one per line)
    #print("\n".join(dir_list))
    for line in dir_list:
        print(line)
if __name__ == "__main__":
    main()
