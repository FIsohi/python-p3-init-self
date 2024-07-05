#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    john = Person("John")
    print(john.name)  # Output: John

    jane = Person("Jane")
    print(jane.name)  # Output: Jane

