# Project 6: Simple Calculator
# Author: Gül İfdal ALDEMİR
# Date: 19 July 2026

# Toplama işlemini yapan fonksiyon
def add(a, b):
    return a + b
# Çıkarma işlemini yapan fonksiyon
def subtract(a, b):
    return a - b
# Çarpma işlemini yapan fonksiyon
def multiply(a, b):
    return a * b
# Bölme işlemini yapan fonksiyon
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
# Üs alma işlemini yapan fonksiyon
def power(a, b):
    return a ** b
# Mod alma işlemini yapan fonksiyon
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b

# Kullanıcının sayısal girdi yapmasını sağlayan yardımcı fonksiyon
# 'exit' girilirse program kapatılır.
def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print(" Thank you for using the calculator. Goodbye! ")
            exit()
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value or 'exit' to quit.")

print()
print("=====================================================================================")
print("                               SIMPLE CALCULATOR                                     ")
print("=====================================================================================")
print("Hello! Welcome to the Simple Calculator. ")
print(" You can perform different mathematical operations. ")
print("Type 'exit' anytime to close the calculator. ")
print("======================================================================================")

#Kullanıcı çıkış yapana kadar program çalışmaya devam eder
while True:

    print()
    print("Available Operations: ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6. modulus")
    print("Type 'exit' to quit. ")

    operations = input(" Choose an operations: ").lower()

    if operations == "exit":
        print(" Thank you for using the calculator. Goodbye! ")
        break
    if operations not in [
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "modulus"
    ]:
        print("Invalid operation. Please try again. ")
        continue

    # Kullanıcıdan sayıları alıyoruz
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    #Seçilen işleme göre sonucu hesaplıyoruz
    if operations == "add":
        result = add(num1, num2)
    elif operations == "subtract":
        result = subtract(num1, num2)
    elif operations == "multiply":
        result = multiply(num1, num2)
    elif operations ==  "divide":
        result = divide(num1, num2)
    elif operations == "power":
        result = power(num1, num2)
    elif operations == "modulus":
        result = modulus(num1, num2)
    
    print()

    # Sonucu ekrana yazdırıyoruz
    if isinstance(result, str):

        
        print(result)
    else:
        print("- -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - ")
        print(f"Result: {result:.2f}")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("================================================")
        








