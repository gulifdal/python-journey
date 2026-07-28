
# Topic 20 Practice Project: Student Data Processor
# Author: Gül İfdal ALDEMİR
# Date: July 28, 2026
#
# This project practices data processing with:
# lists, tuples, sets, dictionaries,
# loops, conditions, and comprehensions.
#
# The goal is to organize student data,
# transform information, filter data,
# and create useful summaries.

print()
print("==================================================")
print("          STUDENT DATA PROCESSOR")
print("==================================================")
print()


print("1. STUDENT DATA")

# A dictionary stores each student's name and age.
students = {
    "Gül": 21,
    "Erva": 16,
    "Ayşe": 8,
    "Betül": 6
}

print("Students:", students)


print()
print("2. STUDENT NAMES")

# A list comprehension extracts all student names.
student_names = [
    name
    for name in students
]

print("Student names:", student_names)


print()
print("3. STUDENT AGES")

# A list comprehension extracts all student ages.
student_ages = [
    age
    for age in students.values()
]

print("Student ages:", student_ages)


print()
print("4. STUDENTS UNDER 18")

# A dictionary comprehension filters students
# who are younger than 18.
students_under_18 = {
    name: age
    for name, age in students.items()
    if age < 18
}

print("Students under 18:", students_under_18)


print()
print("5. ADULT STUDENTS")

# A dictionary comprehension filters students
# who are 18 years old or older.
adult_students = {
    name: age
    for name, age in students.items()
    if age >= 18
}

print("Adult students:", adult_students)


print()
print("6. UNIQUE AGES")

# A set comprehension creates a collection
# containing only unique student ages.
unique_ages = {
    age
    for age in students.values()
}

print("Unique ages:", unique_ages)


print()
print("7. AGE CATEGORIES")

# A dictionary comprehension with if-else
# categorizes each student as adult or under 18.
age_categories = {
    name: "Adult" if age >= 18 else "Under 18"
    for name, age in students.items()
}

print("Age categories:", age_categories)


print()
print("8. STUDENT SUMMARY")

# A tuple stores fixed summary information.
student_summary = (
    len(students),
    len(adult_students),
    len(students_under_18)
)

print("Total students:", student_summary[0])
print("Adult students:", student_summary[1])
print("Students under 18:", student_summary[2])


print()
print("9. DATA PROCESSING SUMMARY")

# This section displays the final processed data.
print("Names:", student_names)
print("Ages:", student_ages)
print("Unique ages:", unique_ages)
print("Adults:", adult_students)
print("Under 18:", students_under_18)
print("Age categories:", age_categories)


print()
print("==================================================")
print("        END OF STUDENT DATA PROCESSOR")
print("==================================================")
print()

