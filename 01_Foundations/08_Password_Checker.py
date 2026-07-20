# ==========================================
# Topic 08: Password Checker
# Author: Gül İfdal ALDEMİR
# Date: 14 July 2026
#
# Description:
# Learning how to use while loops
# to repeat an action until the
# correct password is entered.
# ==========================================

print()
print("====================================")
print("       PASSWORD CHECKER")
print("====================================")

# Doğru şifreyi belirliyoruz.

correct_password = "python1234"

# İlk başta kullanıcıdan herhangi bir giriş alınmadığı için
# password değişkenini boş oluşturuyoruz.

password = ""

#Kullanıcıdan doğru şifreyi girene kadar döngü devam eder.

while password != correct_password:
        
        password = input("Enter your password: ")

        if password != correct_password: 
            print("Access denied. Please try aagain.")
        
print()
print("Access granted!")
print("Welcome!")

print()
print("===============================")

# =======================
# End of Topic 08
# ======================
                  
