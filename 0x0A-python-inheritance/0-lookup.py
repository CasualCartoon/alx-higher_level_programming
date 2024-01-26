#!/usr/bin/python3

def lookup(obj):
    return dir(obj)

if __name__ == "__main__":
    your_object_here = {}
    result = lookup(your_object_here)
    print(result)
