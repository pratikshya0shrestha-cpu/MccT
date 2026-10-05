print("TASK 7: Nested Conditional Statement (Login System)")
print("=" * 50)

username = input("Enter username: ")
password = input("Enter password: ")

if username == "pratikshya":
    if password == "pratikshya123":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")
