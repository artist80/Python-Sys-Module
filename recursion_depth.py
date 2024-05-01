usr/bin/env python3

import sys

def max_recursion_depth():
    depth = sys.getrecursionlimit()
    print("Maximum recursion depth:", depth)

def set_custom_recursion_depth(new_depth):
    sys.setrecursionlimit(new_depth)
    print("Custom recursion depth set to:", new_depth)

def recursive_function(n):
    if n <= 0:
        return 0
    return n + recursive_function(n - 1)

if __name__ == "__main__":
    max_recursion_depth()

    # Set a custom recursion depth
    new_depth = 1500  # Change this to your desired depth
    set_custom_recursion_depth(new_depth)

    # Test the effect of custom recursion depth
    try:
        result = recursive_function(1000)  # Change this to a value that exceeds the new depth
        print("Result of recursive function:", result)
    except RecursionError:
        print("Recursion depth exceeded.")