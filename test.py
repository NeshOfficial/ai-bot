import os
#  define all ₮he functions
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        return "File not found"

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    return "Content written to file"

class Person:
    def __init__(self, name, age):
        self

import os

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        return "File not found"

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    return "Content written to file"

class Person:
    def __init__(self, name, age):
        self
