print("TASK 6: Logical Operators (and, or, not)")
print("=" * 50)

# Using 'and' for voting eligibility
voter_age = int(input("Enter your age: "))
citizenship = input("Do you have citizenship? (yes/no): ")

if voter_age >= 18 and citizenship == "yes":
    print("Eligibility: You are eligible to vote.")
else:
    print("Eligibility: You are NOT eligible to vote.")

# Using 'or' for student service access
role = input("Enter your role (student/staff/other): ")
if role == "student" or role == "staff":
    print("Access: You can access the student service.")
else:
    print("Access: Access denied.")

# Using 'not'
is_restricted = False
if not is_restricted:
 print("Not Operator Example: Access is granted (not restricted).")