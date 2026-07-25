
#Topic 16 Practice: Personal Profile Manager
#Author: Gül İfdal ALDEMİR
#Date: 23 July 2026

#This practice project applies the concepts learned in Topic 16:
#dictionaries, key-value pairs, accessing values,
#adding data, updating data, deleting data,
#dictionary methods, loops, and functions.


print()
print("==========================================================")
print(" PERSONAL PROFILE MANAGER")
print("==========================================================")
print()

#This function creates and returns a personal profile dictionary.

def create_profile(name, age, university, goal):
    profile = {
        "name": name,
        "age": age,
        "university": university,
        "goal": goal,
    }
    return profile


#We create a profile using the function
profile = create_profile(
    "Gül",
    22,
    "International Balkan University",
    "AI Engineer",
)

print("1. PROFILE")
print(profile)

print()
print("2. ACCESSING PROFILE DATA")

#We access dictionary values using their keys
print("Name:", profile["name"])
print("Age:", profile["age"])
print("University:", profile["university"])
print("Goal:", profile["goal"])

print()
print("3. ADDING NEW DATA")

#We add new key-value pairs to the dictionary.
profile["language"] = "Python"
profile["status"] = "Learning"

print()
print("4. UPDATING DATA")

#We update an existing value.
profile["status"] = "Learning and Building"
print("Updated status:", profile["status"])

print()
print("5. USING GET()")

#Get() safely accesses a value using its key.
print("Language:", profile.get("language"))
print("Email:", profile.get("email", "Email not provided"))

print()
print("6. CHECKING KEYS")

#We check whether a key exists in the dictionary.
if "goal" in profile:
    print("Goal information exists.")

if "email" not in profile:
    print("Goal information does not exist.")

print()
print("7. DICTIONARY METHODS")

#Keys() returns all keys.
print("Keys:", profile.keys())

#Values() returns all values.
print("Values:", profile.values())

print("Items:")
for key, value in profile.items():
    print(f"{key}: {value}")


print()
print("8. LOOPING THROUGH THE PROFILE")

#We use items() to acces each key and value.

for key, value in profile.items():
    print(key, ".", value)


print()
print("9. REMOVING DATA")

# pop() removes a key-value pair and returns the removed value.

removed_status = profile.pop("status")

print("Removed status:", removed_status)

print()
print("10. FINAL PROFILE")

#We display the final version of the profile.


print(profile)

print()
print("==========================================================")
print(" END OF PRACTICE PROJECT")
print("==========================================================")
print()