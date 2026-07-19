# Project 4: IBU Grade Calculator
# Author: [Gül İfdal ALDEMİR]
# Date: 17 July 2026

#This program calculates the ECTS letter grade
#according to the IBU grading system based on the user's input for activity, midterm, and final grades.

print()
print("Welcome to the IBU Grade Calculator!")

# Kullanıcıdan dönem içi notunu alıyoruz
activity_points = float(input("Enter the activity grade: "))
midterm_points = float(input("Enter the midterm grade: "))

#Finale girme hakkı için dönem içi puanını hesaplıyoruz
semester_score = (activity_points * 0.25) + (midterm_points * 0.35)

#Finale girme hakkını kontrol ediyoruz
if semester_score < 10:
    print("You are NOT eligible to take the final exam.")
    print(f"Your semester score is: {semester_score:.2f}")

else:
    # Kullanıcı finale girme hakkına sahipse final notunu alıyoruz
    final_points = float(input("Enter the final grade: "))
    # Genel başarı notunu hesaplıyoruz
    total_grade = (
        (activity_points * 0.25)
        + (midterm_points * 0.35)
        + (final_points * 0.4)
    )

    #Saysal notu belirliyoruz
    if total_grade >= 95:
        numeric_grade = 10
    elif total_grade >= 85:
        numeric_grade = 9
    elif total_grade >= 75:
        numeric_grade = 8
    elif total_grade >= 65:
        numeric_grade = 7
    elif total_grade >= 50:
        numeric_grade = 6
    else:
        numeric_grade = 5

    print()
    print("=================================================================================")
    print("                        IBU ACADEMİC REPORT                                  ")
    print("=================================================================================")

print(f"Activity Grade : {activity_points}")
print(f"Midterm Grade : { midterm_points}")
print(f"Final Grade : {final_points}")
print(f"Course Average : {total_grade}")
print(f"Numerical Grade : {numeric_grade}")

#Geçme/Kalma durumunu kontrol ediyoruz
if final_points < 40:
    print("Status        : FAILED")
    print("Reason        : Final exam grade is below 40.")
elif total_grade >= 50:
    print("Status        : PASSED")
else:
    print("Status        : FAILED")
    print("Reason        : Course average is below 50.")
    


