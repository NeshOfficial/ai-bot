
from functools import wraps

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def fetch_data_from_api(url):
    # response = requests.get(url)
    # response.raise_for_/assetsstatus()
    # return response.json()

    return [num for num in numbers if num % 2 == 0]
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

@exception_handler
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
    print(f"Data saved to {filename}")

class Calculator:
    def __init__(self):
        self.history = []

    def add_to_history(self, operation, result):
        self.history.append((operation, result))

    def show_history(self):
        return self.history

    def clear_history(self):
        self.history = []
    @exception_handler
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.add_to_history(f"divide({a}, {b})", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.add_to_history(f"multiply({a}, {b})", result)
        return result

if __name__ == "__main__":
    # API Data fetching
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data_from_api(url)

    # Process numbers
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = filter_even_numbers(numbers)
    squared_numbers = square_numbers(numbers)

    # Save processed data to file
    save_data_to_file(even_numbers, "even_numbers.txt")
    save_data_to_file(squared_numbers, "squared_numbers.txt")

    # Calculator operations
    calc = Calculator()
    print(calc.divide(10, 2))
    print(calc.multiply(5, 3))
    print(calc.show_history())

    # Display history
    calc.clear_history()
    print(calc.show_history())
