import random

def generate_random_numbers(count, start, end):
    # Generate a list of random numbers
    random_numbers = [random.randint(start, end) for _ in range(count)]
    return random_numbers

def print_random_operations(random_numbers):
    # Print the generated random numbers
    print("Generated Random Numbers:", random_numbers)

    # Calculate and print the sum of the random numbers
    total_sum = sum(random_numbers)
    print("Sum of Random Numbers:", total_sum)

    # Calculate and print the average of the random numbers
    average = total_sum / len(random_numbers)
    print("Average of Random Numbers:", average)

    # Find and print the maximum and minimum numbers
    max_number = max(random_numbers)
    min_number = min(random_numbers)
    print("Maximum Number:", max_number)
    print("Minimum Number:", min_number)

if __name__ == "__main__":
    # Example usage
    count = 10  # Number of random numbers to generate
    start = 1   # Start of the range (inclusive)
    end = 100   # End of the range (inclusive)

    random_numbers = generate_random_numbers(count, start, end)
    print_random_operations(random_numbers)
