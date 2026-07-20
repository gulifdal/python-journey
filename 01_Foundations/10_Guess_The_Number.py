# ==========================================
# Topic 10: Guess The Number
# Author: Gül İfdal ALDEMİR
# Date: 15 July 2026
#
# Description:
# Learning how to use random numbers,
# while loops, and conditional statements
# by creating a simple guessing game.
# ==========================================

import random

print()
print("====================================")
print("       GUESS THE NUMBER")
print("====================================")

# Bilgisayar 1 ile 20 arasında rastgele bir sayı seçiyor.

secret_number = random.randint(1, 20)

print("I have choosen a number between 1 and 20.")
print("Can you guess it? ")

# Kullanıcı doğru tahmini yapana kadar oyun devam eder.

while True:
    guess = int(input("Enter your guess: "))

    # Girilen sayının geçerli olup olmadığını kontrol ediyoruz.

    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    # Tahmini kontrol ediyoruz.

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number.")
        break


    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print()
print("==========================")

#===================
# End of Topic 10
#===================



