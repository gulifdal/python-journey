# Topic 19 Practice: Comprehensions
# Author: Gül İfdal ALDEMİR
# Date: 26 July 2026
#
# This practice project combines:
# lists, dictionaries, sets, loops,
# and comprehensions.



print()
print("==========================================================")
print("       TOPIC 19 - COMPREHENSION PRACTICE PROJECT")
print("==========================================================")
print()


print("1. STUDENT DATA")

# We store student information inside a list of dictionaries.


students = [
    {
        "name": "Gül",
        "age": 21,
        "university": "International Balkan University (IBU)",
        "goal": "AI Engineer"
    },
    {
        "name": "Erva",
        "age": 16,
        "university_goal": "Istanbul Technical University (ITU)",
        "department_goal": "Aeronautical Engineering",
        "status": "YKS Student"
    }
]

print(students)


print()
print("2. STUDENT NAMES")

# We use list comprehension to collect student names.

student_names = [
    student["name"]
    for student in students
]

print("Names:", student_names)


print()
print("3. STUDENT AGES")

# We use list comprehension to collect student ages.

student_ages = [
    student["age"]
    for student in students
]

print("Ages:", student_ages)


print()
print("4. STUDENTS UNDER 18")

# We filter students who are under 18.

under_18 = [
    student["name"]
    for student in students
    if student["age"] < 18
]

print("Students under 18:", under_18)


print()
print("5. STUDENT GOALS")

# We use dictionary-style access carefully because
# the two student dictionaries have different keys.


goals = [
    student["goal"]
    for student in students
    if "goal" in student
]

print("Goals:", goals)


print()
print("6. UNIQUE UNIVERSITIES")

# We create a set to store unique university information.

universities = {
    student.get("university")
    for student in students
    if student.get("university")
}

print("Universities:", universities)


print()
print("7. STUDENT PROFILE SUMMARY")

# We create a dictionary comprehension using student names
# as keys and ages as values.


student_age_map = {
    student["name"]: student["age"]
    for student in students
}

print("Student age map:", student_age_map)


print()
print("8. STUDENT STATUS")

# We use get() to safely access optional information.

student_status = {
    student["name"]: student.get("status", "Not specified")
    for student in students
}

print("Student status:", student_status)


print()
print("9. COMPREHENSION SUMMARY")

print("Student names:", student_names)
print("Students under 18:", under_18)
print("Unique universities:", universities)
print("Student age map:", student_age_map)
print("Student status:", student_status)


print()
print("==========================================================")
print("          END OF COMPREHENSION PRACTICE PROJECT")
print("==========================================================")
print()