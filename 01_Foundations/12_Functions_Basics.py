# ==========================================
#Day 12: Functions Basics
# Author: Gül İfdal ALDEMİR
# Date: 19 July 2026
#
# Description:
# Learning how to create and use
# functions by generating an
# International Balkan University
# email address.
# ==========================================

print()
print("==================================")
print("      IBU EMAIL GENERATOR")
print("==================================")

# E-posta oluşturan fonksiyon
def create_email(first_name, middle_name, last_name):
	"""Create an IBU email address from first middle and last name."""

	f = first_name.strip().lower()
	m = middle_name.strip().lower()
	l = last_name.strip().lower()
	return f"{f}.{m}.{l}@ibu.edu.mk"

# Kullanıcıdan isim bilgilerini alıyoruz
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name (or press Enter to skip): ")
last_name = input("Enter your last name: ")

# Girilen bilgileri kullanarak e-posta adresini oluşturuyoruz
email = create_email(first_name, middle_name, last_name)

print()

#Oluşturulan e-posta adresini ekrana yazdırıyoruz

print("Your university email is:")
print(email)

print()
print("====================================")

# ==========================================
# End of Topic 12
# ==========================================