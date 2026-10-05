print("TASK 5: Grade using if-elif-else")
print("=" * 50)

student_marks = float(input("Enter marks to check your grade: "))

if student_marks >= 90:
    grade = "A+"
elif student_marks >= 80:
    grade = "A"
elif student_marks >= 70:
    grade = "B"
elif student_marks >= 60:
    grade = "C"
elif student_marks >= 50:
    grade = "D"
elif student_marks >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Marks: {student_marks} | Grade: {grade}")