#!/usr/bin/env python3

import sys

# Print the original system path
print("Original system path:")
for path in sys.path:
    print(path)

# Add a new directory to the system path
new_directory = "/path/to/new/directory"
sys.path.append(new_directory)

# Print the modified system path
print("\nModified system path:")
for path in sys.path:
    print(path)
