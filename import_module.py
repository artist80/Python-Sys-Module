usr/bin/env python3 

import sys

def import_module(module_name):
    if module_name in sys.modules:
        # If the module is already imported, return it from sys.modules
        return sys.modules[module_name]
    else:
        try:
            # If the module is not in sys.modules, import it
            module = __import__(module_name)
            # Add the imported module to sys.modules
            sys.modules[module_name] = module
            return module
        except ImportError:
            print("Error: Module '{}' not found.".format(module_name))
            return None

if __name__ == "__main__":
    module_name = input("Enter module name to import: ")
    imported_module = import_module(module_name)
    if imported_module:
        print("Module '{}' imported successfully.".format(module_name))