# Project: Guess the Secret Number Game
# Author: Gül İfdal ALDEMİR
# Date: 16 July 2026

import random

# Kullanıcıdan tekraroynamak istediği sürece oyun devam edecek
play_again = "y"
while play_again == "y":

    print()
    print("Welcome to the Guess the Secret Number Game!")
    print("You have 5 attempts to guess the secret number between 1 and 20.")

     
     # Bilgisiyar tarafından 1 ile 20 arasında rastgele bir sayı seçiliyor
    secret_number = random.randint(1, 20)
    #kullanıcının 5 tahmin hakkı var
    for attempt in range(1, 6):
        

        # Kullanıcının 5 tahmin hakkı var ve her tahminin ardından kullanıcıya geri bildirim veriliyor
        guess = int(input(f"Attempt {attempt}/5 - Guess the secret number between 1 and 20: "))
        # Kullanıcıdan tahmini alınıyor
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue
        # Tahminin doğru olup olmadığı kontrol ediliyor
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number in {attempt} attempts.")
            break
    # Tahminin yakın olup olmadığı kontrol ediliyor
        elif abs(guess - secret_number) <= 2:
            print("You're very close! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        # Tahmin hakkı bittiğinde kullanıcıya kaybettiği mesajı gösteriliyor 
            if attempt == 5 and guess != secret_number:
             print(f"You lost! The secret number was {secret_number}")  
            
#Kullanıcı tekrar oynamak istediği sürece oyun devam edecek, aksi takdirde oyun bitecek
    play_again = input("Do you want to play again? (y/n): ").lower()

    