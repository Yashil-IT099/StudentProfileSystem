students = []

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
age = input("Enter age: ")

student = {
    "name": name,
    "roll": roll,
    "branch": branch,
    "age": age
}

students.append(student)

print("\nStudent Profile")
print("Name:", name)
print("Roll:", roll)
print("Branch:", branch)
print("Age:", age)

print("Student Profile System")
print("Student profile updated successfully")