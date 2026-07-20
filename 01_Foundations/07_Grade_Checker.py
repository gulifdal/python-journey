# ==========================================
# Topic 07: Grade Checker
# Author: Gül İfdal ALDEMİR
# Date: 13 July 2026
#
# Description:
# Learning how to use conditional
# statements to evaluate exam scores.
# ==========================================

print()
print("====================================")
print("         GRADE CHECKER")
print("====================================")

# Kullanıcıdan sınav notunu alıyoruz.

score = int(input("Enter your score (0-100): "))
print()

# Girilen notun geçerli olup olmadığını kontrol ediyoruz.

if score < 0 or score > 100:
     print("Invalid score. ")

# Notu belirlenen aralıklara göre değerlendiriyoruz.

elif score >= 90:
    print("Grade: Excellent ")

elif score >= 70:
     print("Grade: Good ")

elif score  >= 50:
     print("Grade: Pass ")

else:
     print("Grade: Failed ")

print()
print("==========================================")

#=========================
# End of Topic 07
#=========================