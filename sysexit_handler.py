#!/usr/bin/env python3

import sys

def exit_handler():
    print("Exiting the program gracefully.")

# Register exit handler
sys.exitfunc = exit_handler

if __name__ == "__main__":
    # Your main program logic here
    print("Running the program...")
    # Simulating some work
    for i in range(5):
        print("Working...", i)
    
    # Exiting the program
    sys.exit(0)
