#Day 3: Mathematical operations

#Take input of 2 numbers from the user and print the sum,
#product, and the first number raised to the power of 10.
#

def main():
	try:
		a = float(input("Enter first number: ").strip())
		b = float(input("Enter second number: ").strip())
	except ValueError:
		print("Invalid input. Please enter numeric values.")
		return

	sum_val, product, power10 = compute(a, b)

	print(f"Sum: {sum_val}")
	print(f"Product: {product}")
	print(f"{a} raised to the power 10 is: {power10}")


def compute(a, b):
	"""Compute sum, product, and a**10 for given numbers.

	Returns a tuple: (sum, product, a_power_10)
	"""
	sum_val = a + b
	product = a * b
	power10 = a ** 10
	return sum_val, product, power10


if __name__ == "__main__":
	main()

