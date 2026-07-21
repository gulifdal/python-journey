# ==========================================
# # Topic 14 - Functions in Practice
# # Author: Gül İfdal ALDEMİR
# # Date: 21 July 2026
# #
# # Description:
# # A practical Python topic focused on functions,
# # parameters, function calls, and return values.
# #
# # This topic is part of my Python learning journey.
# ==========================================


# This function creates a personalized introduction message.
# Bu fonksiyon kişiselleştirilmiş bir tanıtım mesajı oluşturur.

def create_incroduction(name, dream_job, current_goal):
    return (
        f"Hello, {name}!\n\n"
        f"Your dream job is to become a {dream_job}.\n"
        f"Your current goal is to {current_goal}.\n\n"
        "Keep learning and keep building."

    )

# Get information from the user.

name = input("What is your name? ")
dream_job = input("What is your dream job? ")
current_goal = input("What isyour current goal? ")

# Create the personalized message using the function.

incroduction = create_incroduction(
    name,
    dream_job,
    current_goal
)

# Display the final message.

print()
print("=======================================================")
print("                PERSONAL INTRODUCTION")
print("========================================================")
print()
print("=========================================================")
print(f"{name}")
print("==========================================================")


# ====================
# End of Topic 14
# ===================