
student_marks = {
    "Ravi": 85,
    "Sneha": 92,
    "Aman": 76,
    "Kiran": 89,
    "Priya": 95
}


name = input("Enter the student's name: ")


if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found in the record.")
