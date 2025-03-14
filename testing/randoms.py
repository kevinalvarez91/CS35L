#!/usr/bin/python
import argparse
import random
import sys  # Import sys for sys.exit()

def main():
    # Argument Parser Setup
    parser = argparse.ArgumentParser(description="This program is for random checker")
    parser.add_argument("-r", "--range", type=str, required=True, help="Giving range of possible combinations (e.g., 1-100)")
    #required=True to make sure that you must put it
    parser.add_argument("-t", "--tries", type=int, help="Giving the number of tries for the user")

    args = parser.parse_args()

    # Ensure `args.range` is in correct format
    try:
        start, end = map(int, args.range.split('-'))
        if start >= end:
            print("Error: The start of the range must be less than the end.")
            sys.exit(1)
    except ValueError:
        print("Error: Range must be in 'start-end' format (e.g., 1-100).")
        sys.exit(1)

    # Generate a random number within the given range
    number = random.randint(start, end)
    counter = 0  # Counter for user attempts

    print("🎲 Random Number Generator Checker 🎲")

    if args.tries:
        while counter < args.tries:
            try:
                usrNum = int(input(f"Attempt {counter+1}/{args.tries}: Enter a number between {start}-{end}: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if usrNum == number:
                print("🎉 You got it! 🎉")
                sys.exit(0)
            else:
                print("❌ Incorrect! Try again.")
            counter += 1

        # If user runs out of tries
        print(f"😢 You ran out of tries! The correct number was {number}.")
        sys.exit(0)

    else:
        print("You have unlimited tries! Good luck!")
        while True:
            try:
                num = int(input(f"Enter a number between {start}-{end}: "))  # Convert input to integer
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if num == number:
                print("🎉 You got it! 🎉")
                sys.exit(0)  # No need for break

if __name__ == "__main__":
    main()
