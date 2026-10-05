print("TASK 3: Arithmetic Operations")
print("=" * 50)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nResults of Arithmetic Operations for {num1} and {num2}:")
print(f"Addition (+)       : {num1} + {num2} = {num1 + num2}")
print(f"Subtraction (-)    : {num1} - {num2} = {num1 - num2}")
print(f"Multiplication (*) : {num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"Division (/)       : {num1} / {num2} = {num1 / num2:.2f}")
    print(f"Modulus (%)        : {num1} % {num2} = {num1 % num2}")
    print(f"Floor Division (//): {num1} // {num2} = {num1 // num2}")
else:
    print("Division,Modulus and Floor Division cannot be performed (division by zero).")
print(f"Power (**) : {num1} ** {num2} = {num1 ** num2}")
