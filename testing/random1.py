#!/opt/homebrew/bin/python3
import random

def random_shuffle(x):
    for sub_list in x:
        random.shuffle(sub_list)
    random.shuffle(x)


def main():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    random_shuffle(x)
    print(x)

if __name__ == "__main__":
    main()
