#!/opt/homebrew/bin/python3
import sys
def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            print("".join(sorted(file[0:len(line) - 1]))) #Note: when splicing the start is inclusive, while the end is exclusive
            






if __name__ == "__main__":
    main()