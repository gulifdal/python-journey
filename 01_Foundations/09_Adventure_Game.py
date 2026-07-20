# ==========================================
# Topic 09: Adventure Game
# Author: Gül İfdal ALDEMİR
# Date: 14 July 2026
#
# Description:
# Learning how to use if and elif
# statements by creating a simple
# text-based adventure game.
# ==========================================

print()
print("====================================")
print("         ADVENTURE GAME")
print("====================================")

# Oyunun başlangıç hikayesini gösteriyoruz.

print("Welcome to the Adventure Game!")
print()

#Kullanıcıdan seçim alıyoruz.

choice = input(
    "You are in a dark forest.  \n"
    "Do you want to go left or right? "
    ).lower()

print()

#Kullanıcıdan seçimine göre farklı senaryolaroluşturuyoruz.

if choice == "left":
    print("You encounter a friendly elf.") 
    print("The elf  gives you a treasure map!")
    print("Congratulations! Your adventure continues.")

elif choice == "right":

    print("You fall into a trap set by goblins.") 
    print("Game over!")

else:
    print("Invalid choice. ")
    input("Please choose 'left' or 'right'.")

print()
print("==============================")

#=======================
# End of Topic 09
#=======================

