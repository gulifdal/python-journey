# ==========================================
# Topic 02: User Input
# Author: Gül İfdal ALDEMİR
# Date: 09 July 2026
#
# Description:
# Learning how to get information
# from the user using input().
# ==========================================

print()
print("====================================")
print("           USER INPUT")
print("====================================")

# Kullanıcıdan temel bilgileri alıyoruz.

name = input("What is your name? ")
age = input("How old are you? " )
country = input("Where are you from? " )
major = input("What is your major? ")

# Kullanıcıdan alınan bilgileri düzenli bir şekilde gösteriyoruz.

print()
print("================= STUDENT PROFILE ================")

print("Name          :", name)
print("Age           :", age)
print("Country       :", country)
print("Major         :", major)

print("===================================================")

# Kullanıcıyı kişisel bir mesaj ile selamlıyoruz.

print()
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You are from {country}.")
print(f"You study {major}.")

# ===============================
# End of the Topic 02
# ===============================

