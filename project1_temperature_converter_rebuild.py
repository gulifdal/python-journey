# Project 1 - Temperature Converter
# Author: Gül İfdal ALDEMİR
# Date: 16 July 2026 

# kullanıcıdan Celsius cinsinden sıcaklık değerini al
#celsius = float(input("Enter temperature in Celsius: "))
# Fahrenheit cinsine dönüştür
#fahrenheit = (celsius * 9/5) + 32
# sonuçları yazdır
#print(f"{celsius}°C is equal to {fahrenheit}°F")

# --------------------------- BONUS KISMI ------------------------------
# Kullanıcıya seçenekleri gösteriyoruz
print()
print("Temperature Converter Menu:")
print()
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print()
# Kullanıcının seçimini al
choice = int(input("Enter your choice (1 or 2): "))

# Eğer kullanıcı 1'i seçerse Celsius'tan Fahrenheit'a dönüştürme yapıyoruz
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
 # Eğer kullanıcı 2'yi seçerse Fahrenheit'tan Celsius'a dönüştürme yapıyoruz   
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
# Kullanıcı geçersiz bir seçim yaparsa hata mesajı gösteriyoruz
else:
    print("Invalid choice. Please enter 1 or 2.")