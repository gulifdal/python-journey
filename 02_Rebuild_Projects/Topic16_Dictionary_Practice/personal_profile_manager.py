# Topic 16 Mini Project: Personal Profile Manager
# Author: Gül İfdal ALDEMİR
# Date: 23 July 2026
#
# Bu proje dictionaries ve functions konularını
# birlikte kullanarak basit bir kişisel profil yöneticisi oluşturur.
#
# This project combines dictionaries and functions
# to create a simple personal profile manager.


print()
print("==========================================================")
print("             PERSONAL PROFILE MANAGER")
print("==========================================================")
print()


# ----------------------------------------------------------
# FUNCTION 1 - CREATE PROFILE
# ----------------------------------------------------------

def create_profile(name, age, university, goal):
    # This function creates and returns a profile dictionary.
    # Bu fonksiyon bir profile dictionary oluşturur ve döndürür.

    profile = {
        "name": name,
        "age": age,
        "university": university,
        "goal": goal
    }

    return profile


# ----------------------------------------------------------
# FUNCTION 2 - DISPLAY PROFILE
# ----------------------------------------------------------

def display_profile(profile):
    # This function displays all profile information.
    # Bu fonksiyon tüm profil bilgilerini ekrana yazdırır.

    print()
    print("----- PROFILE -----")

    for key, value in profile.items():
        print(f"{key.title()}: {value}")


# ----------------------------------------------------------
# FUNCTION 3 - UPDATE GOAL
# ----------------------------------------------------------

def update_goal(profile, new_goal):
    # This function updates the user's goal.
    # Bu fonksiyon kullanıcının hedefini günceller.

    profile["goal"] = new_goal

    return profile


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

print("Create Your Profile")
print()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
goal = input("Enter your goal: ")


# Create the profile using the function.
# Fonksiyonu kullanarak profili oluşturuyoruz.

profile = create_profile(
    name,
    age,
    university,
    goal
)


# Display the created profile.
# Oluşturulan profili ekrana yazdırıyoruz.

display_profile(profile)


print()
print("Would you like to update your goal?")

update_goal = input("Enter yes or no: ").lower()

if update_goal == "yes" or update_goal == "y":
    new_goal = input("Enter your new goal: ")

    profile["goal"] = new_goal

    print()
    print("Goal updated successfully.")
    print("New goal:", profile["goal"])
else:
    print()
    print("Goal was not updated.")


print()
print("==========================================================")
print("              END OF PERSONAL PROFILE MANAGER")
print("==========================================================")
print()