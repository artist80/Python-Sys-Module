#!/usr/bin/env python3

import sys

def parse_arguments():
    arguments = sys.argv[1:]  # Exclude the script name itself
    parsed_args = {}
    current_key = None
    
    for arg in arguments:
        if arg.startswith('-'):
            current_key = arg.lstrip('-')
            parsed_args[current_key] = True
        elif current_key:
            parsed_args[current_key] = arg
            current_key = None
        else:
            # Handle positional arguments
            if '_positional' not in parsed_args:
                parsed_args['_positional'] = []
            parsed_args['_positional'].append(arg)
    
    return parsed_args

if __name__ == "__main__":
    parsed_args = parse_arguments()
    print("Parsed Arguments:")
    print(parsed_args)
