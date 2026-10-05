import math


def perform_operations(num1, num2):
    # Find the sum and product of two numbers
    print(f"Sum: {num1 + num2}")
    print(f"Product: {num1 * num2}")

    # Find modulus and floor division values
    print(f"Modulus of num1 % 2: {num1 % 2}")
    print(f"Floor division of num2 // 2: {num2 // 2}")

    # Find power and square root
    print(f"Power: {num1 ** num2}")
    print(f"Square root of num1: {math.sqrt(num1):.2f}")


# Example values
perform_operations(16, 4)


