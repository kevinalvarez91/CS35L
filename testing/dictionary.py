#!/opt/homebrew/bin/python3
import random

def random_shuffle(x):
    for sub_list in x:
        random.shuffle(sub_list)
    random.shuffle(x)


def main():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #person = {"name":"Alice", "age":30, "city":"London"}
    person = dict(name="Bob", age=30, city="London")
    person["age"] = 26
    person["job"] = "Engineer"
    del person["city"]
    job = person.pop("job")
    print(person.values()) # dict_values(['Bob', 26])

    for key in person:
        print(key)

    for value in person.values():
        print(value)

    for k, v in person.items():
        print(f"{k}: {v}")



if __name__ == "__main__":
    main()
