# Day 20 Independent Problem Solving
# Topic: Data Processing
# Author: Gül İfdal ALDEMİR
# Date: July 28, 2026
#
# This independent problem-solving practice combines:
# lists, tuples, sets, dictionaries,
# loops, conditions, and comprehensions.
#
# The goal is to process student data,
# filter information, transform values,
# categorize students, and create summaries.


print()
print("==================================================")
print("       DAY 20 - INDEPENDENT PROBLEM SOLVING")
print("==================================================")
print()


# --------------------------------------------------
# 1. STUDENT DATA
# --------------------------------------------------

# A dictionary stores each student's name and age.
# Dictionary anahtar olarak öğrenci isimlerini,
# value olarak yaş bilgilerini saklar.

students = {
    "Gül": 21,
    "Erva": 16,
    "Ayşe": 8,
    "Betül": 6
}

print("1. STUDENT DATA")
print("Students:", students)


# --------------------------------------------------
# 2. GET ALL STUDENT NAMES
# --------------------------------------------------

# A list comprehension extracts all student names.
# List comprehension tüm öğrenci isimlerini çıkarır.

student_names = [
    name
    for name in students
]

print()
print("2. STUDENT NAMES")
print("Student names:", student_names)


# --------------------------------------------------
# 3. GET ALL STUDENT AGES
# --------------------------------------------------

# A list comprehension extracts all student ages.
# List comprehension tüm öğrenci yaşlarını çıkarır.

student_ages = [
    age
    for age in students.values()
]

print()
print("3. STUDENT AGES")
print("Student ages:", student_ages)


# --------------------------------------------------
# 4. FIND STUDENTS UNDER 18
# --------------------------------------------------

# A dictionary comprehension filters students
# who are younger than 18.
# Dictionary comprehension 18 yaşından küçük
# öğrencileri filtreler.

students_under_18 = {
    name: age
    for name, age in students.items()
    if age < 18
}

print()
print("4. STUDENTS UNDER 18")
print("Students under 18:", students_under_18)


# --------------------------------------------------
# 5. FIND ADULT STUDENTS
# --------------------------------------------------

# A dictionary comprehension filters students
# who are 18 years old or older.
# Dictionary comprehension 18 yaş ve üzerindeki
# öğrencileri filtreler.

adult_students = {
    name: age
    for name, age in students.items()
    if age >= 18
}

print()
print("5. ADULT STUDENTS")
print("Adult students:", adult_students)


# --------------------------------------------------
# 6. CREATE UNIQUE AGE SET
# --------------------------------------------------

# A set comprehension creates a collection
# containing unique student ages.
# Set comprehension benzersiz yaşlardan oluşan
# bir set oluşturur.

unique_ages = {
    age
    for age in students.values()
}

print()
print("6. UNIQUE AGES")
print("Unique ages:", unique_ages)


# --------------------------------------------------
# 7. CREATE AGE CATEGORIES
# --------------------------------------------------

# A dictionary comprehension with if-else
# categorizes each student.
# If the student is 18 or older, the category
# is Adult. Otherwise, it is Under 18.

age_categories = {
    name: "Adult" if age >= 18 else "Under 18"
    for name, age in students.items()
}

print()
print("7. AGE CATEGORIES")
print("Age categories:", age_categories)


# --------------------------------------------------
# 8. DOUBLE EVERY STUDENT'S AGE
# --------------------------------------------------

# A list comprehension transforms every age
# by multiplying it by two.
# List comprehension her öğrencinin yaşını
# ikiyle çarparak yeni bir liste oluşturur.

doubled_ages = [
    age * 2
    for age in students.values()
]

print()
print("8. DOUBLED AGES")
print("Doubled ages:", doubled_ages)


# --------------------------------------------------
# 9. GET NAMES OF STUDENTS UNDER 18
# --------------------------------------------------

# A list comprehension filters only the names
# of students who are under 18.
# List comprehension sadece 18 yaşından küçük
# öğrencilerin isimlerini seçer.

under_18_names = [
    name
    for name, age in students.items()
    if age < 18
]

print()
print("9. UNDER 18 STUDENT NAMES")
print("Under 18 names:", under_18_names)


# --------------------------------------------------
# 10. CREATE A FINAL SUMMARY
# --------------------------------------------------

# A tuple stores fixed summary information.
# Tuple sabit özet bilgilerini saklar.

student_summary = (
    len(students),
    len(adult_students),
    len(students_under_18)
)

print()
print("10. FINAL SUMMARY")

print("Total students:", student_summary[0])
print("Adult students:", student_summary[1])
print("Students under 18:", student_summary[2])

print()
print("Student names:", student_names)
print("Student ages:", student_ages)
print("Unique ages:", unique_ages)
print("Adult students:", adult_students)
print("Students under 18:", students_under_18)
print("Age categories:", age_categories)
print("Doubled ages:", doubled_ages)
print("Under 18 names:", under_18_names)


print()
print("==================================================")
print("     END OF INDEPENDENT PROBLEM SOLVING")
print("==================================================")
print()