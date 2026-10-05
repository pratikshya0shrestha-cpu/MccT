print("TASK 4: Pass or Fail")
print("=" * 50)

marks = float(input("Enter your marks: "))

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"Marks: {marks} -- Result: {result}")