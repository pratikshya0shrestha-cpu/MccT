print("TASK 8: Arithmetic + Conditions")
print("=" * 50)

val1 = int(input("Enter first integer: "))
val2 = int(input("Enter second integer: "))

calc_sum = val1 + val2
calc_product = val1 * val2
calc_remainder = val1 % val2 if val2 != 0 else "Undefined (divide by 0)"

print(f"\nCalculations: Sum = {calc_sum}, Product = {calc_product}, Remainder = {calc_remainder}")

# Condition 1: Sum positive or negative
if calc_sum > 0:
    sum_status = "Positive"
elif calc_sum < 0:
    sum_status = "Negative"
else:
    sum_status = "Zero"
print(f"The sum ({calc_sum})is {sum_status}.")

# Condition 2: Product even or odd
if calc_product % 2 == 0:
    prod_status = "Even"
else:
    prod_status = "Odd"
print(f"The product ({calc_product})is {prod_status}.")

# Condition 3: First number greater than second
if val1 > val2:
    print(f"{val1} is greater than {val2}.")
elif val1 < val2:
    print(f"{val1} is less than {val2}.")
else:
    print(f"{val1} is equal to {val2}.")