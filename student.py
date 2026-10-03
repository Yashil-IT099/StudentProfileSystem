students = []

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")

student = {
    "name": name,
    "roll": roll,
    "branch": branch
}

students.append(student)

print("\nStudent Profile")
print("Name:", name)
print("Roll:", roll)
print("Branch:", branch)