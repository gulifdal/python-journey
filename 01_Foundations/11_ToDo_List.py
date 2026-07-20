# ==========================================
# Topic 11: Lists Basics
# Author: Gül İfdal ALDEMİR
# Date: 18 July 2026
#
# Description:
# Learning how to use Python lists
# by creating a simple To-Do List
# application.
# ==========================================

print()
print("====================================")
print("         TO-DO LIST")
print("====================================")

# Görevlerimizi saklayacağımız boş listeyi oluşturuyoruz.

tasks = []

#Kullanıcı çıkış yapana kadar program çalışmaya devam eder.

while True:

    print()
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    print()

    # Yeni görev ekleme
    
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("Your tasks:")
            for task in tasks:
                print(f"- {task}")

    elif choice == "3":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1 and 4.")

print()
print("====================================")

# ==========================================
# End of Topic 11
# ==========================================  