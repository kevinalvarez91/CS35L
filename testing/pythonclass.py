#!/opt/homebrew/bin/python3

class Name:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def printStats(self):
        print(f"My name is {self.name}, {self.age}, {self.major}")

def main():
    d = {'a': 1, 'b': 2}
    d['c'] = 3
    person = Name("Kevin", 20, "Computer Engineering")
    person.printStats()
    a = list(d.keys())
    for i in a:
        print(i, end=" ")


if __name__ == "__main__":
    main()