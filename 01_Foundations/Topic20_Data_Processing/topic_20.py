print()
print("==========================================================")
print("              TOPIC 20 - DATA PROCESSING")
print("==========================================================")
print()


print("1. LIST COMPREHENSION")

# A list comprehension creates a new list
# by applying an expression to each item in an existing list.

numbers = [1, 2, 3, 4, 5]

squares = [
    number ** 2
    for number in numbers
]

print("Numbers:", numbers)
print("Squares:", squares)


print()
print("2. LIST COMPREHENSION WITH IF")

# A condition can be added to a list comprehension.
# In this example, only even numbers are included.


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print("Numbers:", numbers)
print("Even numbers:", even_numbers)


print()
print("3. TRANSFORMING AND FILTERING DATA")


# A list comprehension can transform data
# while also filtering items using a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print("Numbers:", numbers)
print("Even squares:", even_squares)


print()
print("4. FILTERING STUDENT SCORES")

# We can use list comprehensions to filter data
# based on a specific condition.

scores = [45, 78, 92, 61, 34, 88, 100]

passing_scores = [
    score
    for score in scores
    if score >= 60
]

print("All scores:", scores)
print("Passing scores:", passing_scores)


print()
print("5. STUDENT DATA")

# A dictionary stores data using key-value pairs.
# Here, each student's name is the key
# and their age is the value.

students = {
    "Gül": 21,
    "Erva": 16,
    "Ayşe": 8,
    "Betül": 6
}

print("Students:", students)


print()
print("6. DICTIONARY COMPREHENSION")

# A dictionary comprehension creates a new dictionary
# using an expression and a loop.

student_ages = {
    name: age
    for name, age in students.items()
}

print("Student ages:", student_ages)


print()
print("7. FILTERING A DICTIONARY")

# A dictionary comprehension can also filter data.
# Here, we select only students who are 18 or older.

adult_students = {
    name: age
    for name, age in students.items()
    if age >= 18
}

print("Adult students:", adult_students)


print()
print("8. STUDENTS UNDER 18")

# We can filter dictionary data using another condition.
# Here, we select students who are under 18.

young_students = {
    name: age
    for name, age in students.items()
    if age < 18
}

print("Students under 18:", young_students)


print()
print("9. WORKING WITH SET COMPREHENSION")

# A set comprehension creates a set
# and automatically removes duplicate values.

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique_squares = {
    number ** 2
    for number in numbers
}

print("Numbers:", numbers)
print("Unique squares:", unique_squares)


print()
print("10. EXTRACTING STUDENT NAMES")

# We can create a list containing only dictionary keys.
# In this example, we extract all student names.

student_names = [
    name
    for name in students
]

print("Student names:", student_names)

print()
print("11. EXTRACTING STUDENT AGES")

# We can use values() to access all dictionary values.
# Here, we create a list containing all student ages.

student_age_values = [
    age
    for age in students.values()
]

print("Student ages:", student_age_values)


print()
print("12. UNIQUE STUDENT AGES")

# A set comprehension can be used
# to keep only unique student ages.

unique_ages = {
    age
    for age in students.values()
}

print("Unique ages:", unique_ages)

print()
print("13. CHOOSING THE RIGHT DATA STRUCTURE")

# Different data structures are useful for different purposes.

print("LIST -> Ordered and changeable data")
print("TUPLE -> Ordered and fixed data")
print("SET -> Unique data")
print("DICTIONARY -> Key-value data")


print()
print("14. DATA PROCESSING SUMMARY")

# This section summarizes the results
# created from our student data.

print("Student names:", student_names)
print("Students under 18:", young_students)
print("Adult students:", adult_students)
print("Unique ages:", unique_ages)


print()
print("==========================================================")
print("                  END OF TOPIC 20")
print("==========================================================")
print()
