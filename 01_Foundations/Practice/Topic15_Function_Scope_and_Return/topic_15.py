# Topic 15: Function Scope and Return Values
# Author: Gül İfdal ALDEMİR
# Date: 22 July 2026

# This practice focuses on:
# - Functions
# - Parameters
# - Arguments
# - Return values
# - Local variables
# - Function scope
# - Using returned values in other functions

print()
print("==============================================================")
print("          TOPIC 15 - FUNCTION SCOPE & RETURN VALUES")
print("==============================================================")


# ------------------------------------------------------
# 1. BASIC FUNCTION WITH PARAMETERS
# ------------------------------------------------------

def greet_user(name):
    message = f"Hello, {name}! Welcome to topic 15."
    return message


# --------------------------------------------------------------
# 2. FUNCTION WITH A RETURN VALUE
# --------------------------------------------------------------

def calculate_total(price, quantity):
    total = price * quantity
    return total


# --------------------------------------------------------------
# 3. FUNCTION USING ANOTHER FUNCTION'S RETURN VALUE
# --------------------------------------------------------------

def calculate_discount(total, discount_rate):
    discount = total * discount_rate
    return discount

def calculate_final_price(total, discount):
    final_price = total - discount
    return final_price


# --------------------------------------------------------------
# 4. LOCAL VARIABLE AND FUNCTION SCOPE
# --------------------------------------------------------------

def create_user_summary(name, age):
    summary = f"{name} is {age} years old."
    return summary


# --------------------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------------------

print()
print("1. Greeting Function")
print(greet_user("Gül"))


print()
print("2. Total Calculation")

price = 25.0
quantity = 3

total = calculate_total(price, quantity)

print(f"Price: {price:.2f}₺")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}₺")

print()
print("3. Discount Calculation")

discount_rate = 0.10
discount = calculate_discount(total, discount_rate)

print()
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Discount Amount: {discount:.2f}₺")


print()
print("4. Final Price Calculation")

final_price = calculate_final_price(total, discount)

print(f"Original Total: {total:.2f}₺")
print(f"Discount: {discount:.2f}₺")
print(f"Final Price: {final_price:.2f}₺")


print()
print("5. FUNCTION SCOPE")


user_summary = create_user_summary("Gül", 21)

print(user_summary)


print()
print("==============================================================")
print("                    END OF TOPIC 15")
print("==============================================================")