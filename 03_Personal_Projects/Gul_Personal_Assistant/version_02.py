# ==========================================
# # GUL PERSONAL ASSISTANT
# # Version: 0.2
# # Author: Gül İfdal ALDEMİR
# # Date: 21 July 2026
# #
# # Description:
# # The second version of my personal assistant project.
# #
# # In this version, I applied what I learned
# # about functions, parameters, return values,
# # loops, and conditional statements.
# #
# # This project grows together with my Python journey.
# ==========================================


# This function gets the user's name.

def get_user_name():
    name = input("What is your name? ")
    return name

# This function creates a personalized welcome message.

def create_welcome_message(name):
    return f"Welcome, {name}! I'm your personal assistant."

def show_menu():
    print()
    print("===============================================")
    print("              GUL ASSISTANT")
    print("================================================")
    print()
    print("1. Get a welcome message")
    print("2. Exit")
    print()

# This function runs the assistant.

def run_assistant():
    name = get_user_name()

    print()
    print(create_welcome_message(name))

    while True:
        show_menu()

        choice: str = input("Choose an option: ")

        if choice == "1":
            print()
            print(create_welcome_message(name))

        elif choice == "2":
            print()
            print(f"Goodbye, {name}.")
            print("Keep learning and keep building.")
            break

        else:
            print()
            print("Invalid choice. Please try again.")

# This is the main entry point of the application.
# Burası uygulamanın ana başlangıç noktasıdır.

def main():
    run_assistant()


# Run the application

if __name__ == "__main__":
     main()


# ==========================================
# # End of GUL Personal Assistant
# ==========================================

print()
print("==========================================")
print("             Gül İfdal ALDEMİR")
print("==========================================")

