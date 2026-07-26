# Topic 19: Comprehensions
# Author: Gül İfdal ALDEMİR
# Date: 26 July 2026
#
# This topic explores how Python comprehensions work with:
# list comprehensions, conditions, dictionary comprehensions,
# set comprehensions, and converting loops into comprehensions.



print()
print("==========================================================")
print("              TOPIC 19 - COMPREHENSIONS")
print("==========================================================")
print()


print("1. UNDERSTANDDING COMPREHENSIONS")

# A comherehension allows us to create a new collection
# use a shorter and moremredable syntax.

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append((number ** 2))

print("Numbers:", numbers)
print("Squares:", squares)


print()
print("2. LIST COMPREHENSION")

# A list comprehension creates a new list
# in a shorter and more compact way.


squares_comprehension = [number ** 2 for number in numbers]

print("Squares with comprehension:", squares_comprehension)

#[expression for item in collection]
#[number ** 2 for number in numbers]


print()
print("3. LIST COMPREHENSION WITH IF")

# We can use an if condition inside a list comprehension.
# This allows us to filter values while creating a new list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Even numbers with loop:", even_numbers)

# The same logic can be written with a list comprehension.

even_numbers_comprehension = [
    number
    for number in numbers
    if number % 2 == 0
]

# [expression for item in collection if condition]
# [number for number in numbers if number % 2 == 0]

print("Even numbers with comprehension:", even_numbers_comprehension)


print()
print("4. FILTERING STUDENT SCORES")

# We can use list comprehensions to filter data.

scores = [45, 78, 92, 61, 34, 88, 100]

passing_scores = [
    score
    for score in scores
    if score >= 50
]

print("All scores:", scores)
print("Passing scores:", passing_scores)


print()
print("5. LIST COMPREHENSION WITH IF-ELSE")

# We can use if-else to create different values.
# if-else kullanarak farklı değerler oluşturabiliriz.

numbers = [1, 2, 3, 4, 5, 6]

even_or_odd = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print("Numbers:", numbers)
print("Results:", even_or_odd)


print()
print("6. DICTIONARY COMPREHENSION")

# Dictionary comprehension allows us to create
# dictionaries using a compact syntax.
#
# Dictionary comprehension, dictionary'leri
# daha kısa ve kompakt bir syntax ile oluşturmamızı sağlar.

numbers = [1, 2, 3, 4, 5]

squared_numbers = {
    number: number ** 2
    for number in numbers
}

print("Numbers:", numbers)
print("Squared numbers:", squared_numbers)


print()
print("7. DICTIONARY COMPREHENSION WITH CONDITIONS")

scores = {
    "Math": 92,
    "Physics": 85,
    "Python": 95,
    "English": 68
}

high_scores = {
    subject: score
    for subject, score in scores.items()
    if score >= 80
}

print("All scores:", scores)
print("High scores:", high_scores)


print()
print("8. SET COMPREHENSION")

# Set comprehension allows us to create a set
# using a compact comprehension syntax.

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_squares = {
    number ** 2
    for number in numbers
}

print("Numbers:", numbers)
print("Unique squares:", unique_squares)


print()
print("9. COMPREHENSION WITH STRINGS")

# We can use comprehensions to process characters in strings.

name = "Gül"

uppercase_letters = [
    letter.upper()
    for letter in name
]

print("Name:", name)
print("Uppercase letters:", uppercase_letters)


print()
print("10. NORMAL LOOP TO COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

# Normal loop version

doubled_numbers_loop = []

for number in numbers:
    doubled_numbers_loop.append(number * 2)


# Comprehension version

doubled_numbers_comprehension = [
    number * 2
    for number in numbers
]

print("With loop:", doubled_numbers_loop)
print("With comprehension:", doubled_numbers_comprehension)


print()
print("11. COMPREHENSION CHALLENGE")

numbers = [3, 6, 9, 12, 15, 18, 21, 24]


# Task 1: Select numbers divisible by 3.

divisible_by_three = [
    number
    for number in numbers
    if number % 3 == 0
]

print("Divisible by 3:", divisible_by_three)


# Task 2: Create the squares of all numbers.

squared_numbers = [
    number ** 2
    for number in numbers
]

print("Squared numbers:", squared_numbers)


# Task 3: Create squares only for numbers greater than 10.

squares_greater_than_ten = [
    number ** 2
    for number in numbers
    if number > 10
]

print("Squares of numbers greater than 10:", squares_greater_than_ten)



print()
print("12. COMPREHENSION SUMMARY")

# List comprehensions create lists.


print("List comprehension -> creates lists")


# Dictionary comprehensions create dictionaries.


print("Dictionary comprehension -> creates dictionaries")


# Set comprehensions create sets with unique values.

print("Set comprehension -> creates sets")


# Comprehensions can make simple loops shorter and more readable.

print("Comprehensions make simple data transformations more concise.")



print()
print("==========================================================")
print("              END OF TOPIC 19")
print("==========================================================")
print()
