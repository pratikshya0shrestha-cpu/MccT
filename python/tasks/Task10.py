print("TASK 10: Students Marks System")
print("=" * 50)

s_name = input("Enter student name: ")
marks_list = []
subjects = ["Subject 1","Subject 2","Subject 3"]

for subj in subjects:
    mark = float(input(f"Enter marks for {subj}: "))
    marks_list.append(mark)

# Display individual marks using a for loop
print("\nIndividual Marks:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks_list[i]}")

total_marks = marks_list[0] + marks_list[1] + marks_list[2]
average_marks = total_marks / 3

#  Determine Grade
if average_marks >= 90:
    s_grade = "A+"
elif average_marks >= 80:
    s_grade = "A"
elif average_marks >= 70:
    s_grade = "B"
elif average_marks >= 60:
    s_grade = "C"
elif average_marks >= 50:
    s_grade = "D"
else:
    s_grade = "F"

# Check whether student passed all three subjects using 'and'
if marks_list[0] >= 40 and marks_list[1] >= 40 and marks_list[2] >= 40:
    final_result = "Pass"
else:
    final_result = "Fail"

# Output matching required format
print("\n" + "-" * 25)
print(f"Student: {s_name}")
print(f"Total: {total_marks:.0f}" if total_marks.is_integer() else f"Total: {total_marks}")
print(f"Average: {average_marks:.1f}")
print(f"Grade: {s_grade}")
print(f"Result: {final_result}")
print("-" * 25)