# Topic 17 & 18: Data Structures Consolidation
# Author: Gül İfdal ALDEMİR
# Date: July 25, 2026
#
# This topic consolidates the main Python data structures:
# lists, tuples, sets, and dictionaries.
#
# The goal is not only to learn the syntax,
# but also to understand when and why each structure should be used.


print()
print("==========================================================")
print("          TOPIC 17 & 18 - DATA STRUCTURES")
print("==========================================================")
print()

print("1. LISTS")

# Lists are ordered and mutable collections.

skills = [
    "Python",
    "Git",
    "Problem Solving"
]

print("Original list:", skills)

skills.append("AI")

print("After append:", skills)

skills.remove("Git")

print("After remove:", skills)


print()
print("2. TUPLES")

# Tuples are ordered but immutable collections.

student_info = (
    "Gül",
    21,
    "International Balkan University"
)

print("Student information:", student_info)

print("Name:", student_info[0])
print("Age:", student_info[1])
print("University:", student_info[2])

print()
print("3. SETS")

# Sets store unique values.

language = {
    "Python",
    "Python",
    "Java",
    "C++"
}

print("Unique languages:", language)

print()
print("4. DICTIONARIES")

# Dictionaries store data using key-value pairs.

profile = {
    "name": "Gül",
    "age": 21,
    "university": "International Balkan University",
    "goal": "AI Engineer"
}

print()
print("5. COMPARING DATA STRUCTURES")

# Different problems require different data structures.

print("List:", skills)
print("Tuple", student_info)
print("Set:", language)
print("Dictionary:", profile)


print()
print("6. LOOPING THROUGH DATA STRUCTURE")


# We can use loops with different data structures.

print("List items:")

for skill in skills:
    print("-", skill)

print()
print("Dictionary items:")

for key, value in profile.items():
    print(key, ".", value)


print()
print("7. CHECKING MEMBERSHIP")

#The"in" operator checks whether a value exists.

if "Python" in skills:
    print("Python is in the skills list.")
if "Java" in language:
    print("Java is in the languages set.")
if "name" in profile:
    print("Nmae exists in the profile dictionary.")


print()
print("8. CHOOSING THE RIGHT DATA STRUCTURE")

# List:
# Use when order matters and data my change.
# 
# Set:
# Use when unique values are important.
# 
#Dictionary:
# Use when data needs meaningful key-value relationshhips.
#

print("List -> ordered and mutable")
print("Tuple -> ordered and immutable")
print("Set -> unique values")
print("Dictionary -> key-value pairs")

print()
print("9. PRACTICAL EXAMPLE")

#We can combine different data different data structures in one program.

student = {
    "name": "Gül",
    "age": 21,
    "skills": [
        "Python",
        "Git",
        "Problem Solving"
    ],
    "languages": {
        "Python",
        "English",
        "Turkish"
    }
}

print(student)

print("Student name:", student["name"])

print("Skills:")

for skill in student["skills"]:
    print("-", skill)


print()
print("10. DATA STRUCTURE DECISION")

# Ask yourself:
# "What kind of data am I storing?"

print()
print("If I need ordered and changeable data -> LIST")
print("If I need ordered and fixed data -> TUPLE")
print("If I need unique data -> SET")
print("If I need key-value data -> DICTIONARY")


print()
print("==========================================================")
print("              END OF TOPIC 17 & 18")
print("==========================================================")
print()

