# GUL Personal Assistant
# Version 03
# Author: Gül İfdal ALDEMİR
# Date: 22 July 2026

# Topic 15 Connection:
# Function Scope and Return Values


print()
print("==============================================================")
print("                 GUL PERSONAL ASSISTANT")
print("                         VERSION 03")
print("==============================================================")


def create_greeting(name):
    greeting = f"Hello, {name}. I am GUL, your personal assistant."
    return greeting


def create_daily_message(name):
    greeting = create_greeting(name)
    message = f"{greeting} Let's make today meaningful."
    return message


def crreate_focus_message(topic):
    focus_message = f"Today's focus: {topic}"
    return focus_message


print()
print(create_daily_message("Gül"))

print()
print(crreate_focus_message("Learning Python and building GUL"))


print()
print("==============================================================")
print("                    END OF GUL VERSION 03")
print("==============================================================")