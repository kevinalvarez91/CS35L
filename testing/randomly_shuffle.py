#!/opt/homebrew/bin/python3
import random

#Shuffle the mutable sequence in place 

def shuffles(x):
    for i in range(len(x)):
        p = random.randrange(0, len(x))
        x[i], x[p] = x[p], x[i]
    
def main():
    print("x")



if __name__ == "__main__":
    main()