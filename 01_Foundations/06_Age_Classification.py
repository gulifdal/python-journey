# ==========================================
# Topic 06: Age Classification
# Author: Gül İfdal ALDEMİR
# Date: 13 July 2026
#
# Description:
# Learning how to use if, elif,
# and else statements in Python.
# ==========================================

print()
print("====================================")
print("      AGE CLASSIFICATION")
print("====================================")

# Kullanıcıdan yaş bilgisini alıyoruz.

age = int(input("How old are you? "))

# Yaş bilgisine göre kullanıcıyı sınıflandırıyoruz.

if age < 13:
    print("You are a child. )")
elif age < 18:
    print("You are a teenager. ")
else:
    print("You are an adult." )   

print()
print("====================================")

# ====================
# End of Topic 06
# ===================
     