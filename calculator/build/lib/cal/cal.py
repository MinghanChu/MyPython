#!/usr/bin/env python

from basic_operations import add, subtract, multiply, divide
from scientific_operations.trigonometry import sin, cos, tan
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: cal <operation> <arguments>")
        sys.exit(1)

    operation = sys.argv[1]
    args = [float(arg) for arg in sys.argv[2:]]

    if operation == 'add':
        result = add(*args)
    elif operation == 'subtract':
        result = subtract(*args)
    elif operation == 'multiply':
        result = multiply(*args)
    elif operation == 'divide':
        result = divide(*args)
    elif operation == 'sin':
        result = sin(*args)
    elif operation == 'cos':
        result = cos(*args)
    elif operation == 'tan':
        result = tan(*args)
    else:
        print("Error: Invalid operation")
        sys.exit(1)

    print("Result:", result)

if __name__ == '__main__':
    main()
