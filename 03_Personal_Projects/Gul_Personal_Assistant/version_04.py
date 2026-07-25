# GUL Personal Assistant
# Version 0.4
# Author: Gül İfdal ALDEMİR
# Date: 23 July 2026
#
# GUL = Growth • Understanding • Learning
#
# This version introduces dictionaries into GUL.
#
# Bu versiyonda GUL projesine dictionary yapısını ekliyorum.
# Kullanıcı bilgilerini tek tek değişkenler yerine
# bir dictionary içerisinde saklıyorum.


print()
print("==========================================================")
print("             GUL PERSONAL ASSISTANT")
print("                    VERSION 0.4")
print("==========================================================")
print()


# ----------------------------------------------------------
# FUNCTION 1 - CREATE USER PROFILE
# ----------------------------------------------------------

def create_user_profile(name, age, university, goal):
    # This function creates and returns the user's profile.
    # Bu fonksiyon kullanıcının profilini oluşturur
    # ve dictionary olarak geri döndürür.

    user_profile = {
        "name": name,
        "age": age,
        "university": university,
        "goal": goal
    }

    return user_profile


# ----------------------------------------------------------
# FUNCTION 2 - DISPLAY USER PROFILE
# ----------------------------------------------------------

def display_user_profile(user_profile):
    # This function displays the user's profile.
    # Bu fonksiyon kullanıcının profil bilgilerini
    # ekrana yazdırır.

    print()
    print("----- GUL USER PROFILE -----")

    for key, value in user_profile.items():
        print(f"{key.title()}: {value}")


# ----------------------------------------------------------
# FUNCTION 3 - CREATE USER SUMMARY
# ----------------------------------------------------------

def create_user_summary(user_profile):
    # This function creates a short summary
    # using information from the dictionary.
    #
    # Bu fonksiyon dictionary içindeki bilgileri kullanarak
    # kısa bir kullanıcı özeti oluşturur.

    summary = (
        f"Hello {user_profile['name']}! "
        f"You are {user_profile['age']} years old, "
        f"you study at {user_profile['university']}, "
        f"and your goal is to become an {user_profile['goal']}."
    )

    return summary


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

user_profile = create_user_profile(
    "Gül",
    22,
    "International Balkan University",
    "AI Engineer"
)


# Display the profile.
# Profili ekrana yazdırıyoruz.

display_user_profile(user_profile)


# Create and display the user summary.
# Kullanıcı özetini oluşturup ekrana yazdırıyoruz.

user_summary = create_user_summary(user_profile)

print()
print("----- GUL SUMMARY -----")
print(user_summary)


print()
print("==========================================================")
print("             END OF GUL VERSION 0.4")
print("==========================================================")
print()