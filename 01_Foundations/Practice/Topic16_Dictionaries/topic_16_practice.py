

# Topic 16 Practice: Dictionaries
# Author: Gül İfdal ALDEMİR
# Date: 23 July 2026
#
# In this practice file, I will practice dictionaries
# together with functions.


print()
print("==========================================================")
print("              TOPIC 16 - DICTIONARY PRACTICE")
print("==========================================================")
print()


# ----------------------------------------------------------
# PRACTICE 1 - CREATE AND ACCESS A DICTIONARY
# ----------------------------------------------------------

print("1. CREATE AND ACCESS A DICTIONARY")

student = {
    "name": "Gül",
    "age": 22,
    "university": "International Balkan University",
    "goal": "AI Engineer"
}

print("Name:", student["name"])
print("University:", student["university"])
print("Goal:", student["goal"])


# ----------------------------------------------------------
# PRACTICE 2 - ADD AND UPDATE DATA
# ----------------------------------------------------------

print()
print("2. ADD AND UPDATE DATA")

student["language"] = "Python"
student["age"] = 22

print(student)


# ----------------------------------------------------------
# PRACTICE 3 - LOOP THROUGH A DICTIONARY
# ----------------------------------------------------------

print()
print("3. LOOP THROUGH A DICTIONARY")

for key, value in student.items():
    print(key, ":", value)


# ----------------------------------------------------------
# PRACTICE 4 - FUNCTION THAT RETURNS A DICTIONARY
# ----------------------------------------------------------

print()
print("4. FUNCTION THAT RETURNS A DICTIONARY")


def create_student(name, age, goal):
    # This function creates a dictionary and returns it.
    # Bu fonksiyon bir dictionary oluşturur ve geri döndürür.

    student_data = {
        "name": name,
        "age": age,
        "goal": goal
    }

    return student_data


new_student = create_student(
    "Gül",
    22,
    "AI Engineer"
)

print(new_student)


# ----------------------------------------------------------
# PRACTICE 5 - FUNCTION THAT UPDATES A DICTIONARY
# ----------------------------------------------------------

print()
print("5. FUNCTION THAT UPDATES A DICTIONARY")


def update_goal(student_data, new_goal):
    # This function updates the goal value in a dictionary.
    # Bu fonksiyon dictionary içindeki goal value'sunu günceller.

    student_data["goal"] = new_goal

    return student_data


updated_student = update_goal(
    new_student,
    "AI Engineer and Developer"
)

print(updated_student)


# ----------------------------------------------------------
# PRACTICE 6 - FUNCTION THAT DISPLAYS A PROFILE
# ----------------------------------------------------------


print()
print("6. FUNCTION THAT DISPLAYS A PROFILE")


def display_profile(student_data):
    # This function loops through the dictionary
    # and displays each key-value pair.
    #
    # Bu fonksiyon dictionary üzerinde loop kullanır
    # ve her key-value çiftini ekrana yazdırır.

    for key, value in student_data.items():
        print(f"{key}: {value}")



display_profile(updated_student)


print()
print("==========================================================")
print("              END OF TOPIC 16 PRACTICE")
print("==========================================================")
print()