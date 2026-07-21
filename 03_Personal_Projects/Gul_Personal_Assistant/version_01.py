# ==========================================
# 🌷 GÜL — Personal Learning & Growth Assistant
# Version: 0.1
# Author: Gül İfdal ALDEMİR
# Date: 21 July 2026
# ==========================================


# ------------------------------------------
# APP INFORMATION
# ------------------------------------------


# Store basic information about the application.
# Uygulama hakkında temel bilgileri saklar.

app_info = (
    "Gül",
    "v0.1",
    "Personal Learning & Growth Assistant"
)

# -----------------------------------
# LEARNING TOPICS
# -----------------------------------

# Store unique learning topics in a set.
# Benzersiz öğrenme konularını bir set içinde saklar.

learning_topics = {
    "Python",
    "Git",
    "Githup"
}

# ----------------------------------
# TASKS
# ----------------------------------

# Store today's tasks in a list
# Bügünün görevlerini bir liste içinde saklar.

tasks = [
    "Study Python",
    "Practice today's topic",
    "Build Gül"
]

# ---------------------------------
# WELCOME MESSAGE
# ---------------------------------

# Print the main application header

print()
print("=======================================================================")
print("                    🌷 GÜL PERSONAL ASSISTANT")
print("=======================================================================")

# Print a welcome message using the application name.

print()

print("📚 Current Learning Topics:")
for number, topic in enumerate(learning_topics, start = 1):
    print(f"{number}. {topic}")

#--------------------------------
# DISPLAY TODAY'S TASKS
#--------------------------------

# Her görevi bir numara ile gösterir.

print()

print("📝 Today's Tasks:")
for number, task in enumerate(tasks, start = 1):
    print(f"{number}. {task}")

#--------------------------------
# MOTIVATION MESSAGE
#--------------------------------

print()

print("🩵 Keep learning.")
print("💻 Keep building.")
print("🌱 Keep growing.")

#-----------------------------
# END OF APPLICATION
#-----------------------------

print()

print("=========================================================")
print("                    Gül İfdal LDEMİR")
print("==========================================================")



