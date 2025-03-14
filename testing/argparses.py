#!/opt/homebrew/bin/python3
import argparse
import random
import sys
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range",type=str,required=True, help="range")
    parser.add_argument("-t", "--tries", type=int, help="tries")

    args = parser.parse_args()

    start, end = map(int, ((args.range).split("-")))
    tries = args.tries
    randNum = random.randint(start, end)
    counter = 0
    print("Random Number Generator")
    if(args.tries):
        while counter < tries:
            attempt =  int(input(f"Enter a number between {start}-{end}"))
            if attempt == randNum:
                print("You got it! ")
                sys.exit(0)
                break
            counter += 1

        print("You ran out of tries")

    else:
        print("You have unlimited tries")
        while True:
            attemps = int(input(f"Enter a number between {start}-{end}"))
            if attemps == randNum:
                print("You got it! ")
                sys.exit(0)
                break
            else:
                print("Try again")

if __name__ == "__main__":
    main()