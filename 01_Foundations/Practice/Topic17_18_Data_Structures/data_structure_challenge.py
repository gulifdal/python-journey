# Topic 17 & 18 Practice Challenge: Data Structures 
# Author: Gül İfdal ALDEMİR 
# Date: July 25, 2026
#
# This practice project combines:
#list, tuples, sets, and dictionaries.
#
#The goal is to understand which data structure
# should be used for different types of information.


print()
print("==========================================================") 
print(" DATA STRUCTURE PRACTICE CHALLENGE") 
print("==========================================================")
print()

print("1. CREATING ERVA'S PROFILE")

# A dictionary stores Erva's main profile information.
#
#Erva is currently 16 years old and preparing for YKS.
#She wants to enter university next year.

student = {
    "name": "Erva",
    "age": 16,
    "current_status": "YKS Student",
    "university_goal": "Istanbul Technical University (ITU)",
    "department_goal": "Aeronautical Engineering"
}

print(student)


print() 
print("2. ACCESSING DICTIONARY VALUES") 

# We can access specific information using dictionary keys.

print("Name:", student["name"])
print("Age:", student["age"]) 
print("Current status:", student["current_status"]) 
print("University goal:", student["university_goal"])
print("Department goal:", student["department_goal"])


print() 
print("3. CREATING A SKILLS LIST") 

# A list is useful when we have ordered and changeable data.
# These are skills Erva is currently developing.

skills = [ 
    "Mathematics",
    "Physics", 
    "Problem Solving" 
] 

print("Skills:", skills)


print() 
print("4. ADDING A NEW SKILL")

 # Lists allow us to add new values.

skills.append("Time Management") 

print("Updated skills:", skills)


print() 
print("5. CREATING A SET OF PROGRAMMING LANGUAGES")

# A set stores unique values.

programming_languages = {
     "Python" 
}

print("Programming languages:", programming_languages)

print()
print("6. ADDING A NEW PROGRAMMING LANGUAGE")

# We can add a new value to a set.

programming_languages.add("C++")

print("Updated programming languages:", programming_languages)


print()
print("7. CREATING A TUPLE")

# A tuple is ordered but immutable.
#
# This tuple stores fixed information about Erva's relationship 
#
# with the person who created this practice project.

fixed_information = (
    "Gül's sister",
)

print("Fixed information:", fixed_information)



print()
print("8. ACCESSING TUPLE VALUES") 

# We can access tuple values using their index. 

print("Relationship:", fixed_information[0]) 


print()
print("9. ADDING MORE SKILLS")

 # We can add more skills to the list.

skills.append("Communication")

print("Final skills:", skills)


print()
print("10. CHECKING MEMBERSHIP") 

# The "in" operator checks whether a value exists.

if "Python" in programming_languages: print("Erva is learning Python.") 

if "Mathematics" in skills: print("Mathematics is one of Erva's skills.") 

if "university_goal" in student: print("University goal information exists in the profile.")



print()
print("11. LOOPING THROUGH SKILLS")

# We can use a loop to access each skill in the list. 

for skill in skills:
     print("Skill:", skill) 

     

print() 

print("12. LOOPING THROUGH PROGRAMMING LANGUAGES")

 # We can loop through the values stored in a set.

for language in programming_languages: 
     
 print("Language:", language)


print()
print("13. LOOPING THROUGH THE PROFILE")
 
  # items() allows us to access both keys and values. 
  
for key, value in student.items():
     print(key, ":", value)


print() 
print("14. FINAL STUDENT DATA")

 # We can combine different data structures in one dictionary.
 
student["skills"] = skills

student["programming_languages"] = programming_languages 
student["fixed_information"] = fixed_information 

print(student) 

print()
print("==========================================================") 
print(" END OF DATA STRUCTURE CHALLENGE") 
print("==========================================================") 
print()