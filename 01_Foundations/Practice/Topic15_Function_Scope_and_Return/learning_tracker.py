# Topic 15 Practice Project: Personal Learning Tracker
# Author: Gül İfdal ALDEMİR
# Date: 22 July 2026
#
# This mini project practices the function concepts learned in Topic 15.
#
# Bu mini proje Topic 15'te öğrenilen fonksiyon konularını
# pratik etmek amacıyla oluşturulmuştur.
#
# Main concepts:
# - Functions
# - Parameters
# - Arguments
# - Default parameters
# - Keyword arguments
# - Return values
# - Local variables
# - Dictionaries
# - Conditional statements


print()
print("=" * 80)
print("                    PERSONAL LEARNING TRACKER")
print("=" * 80)


# ---------------------------------------------------------------------------
# SECTION 1 — CREATE LEARNING REPORT
# ---------------------------------------------------------------------------

# This function creates a learning report.


# The parameters are:
# name  → learner's name
# topic → learned topic
# score → learning score


def create_learning_report(name, topic, score=0):


    #This variable is local to the funtion.

    if score >= 50:
        status = "Completed"
    else:
        status = "Needs Practice"

    #The function returns a dictionary containimg the report.

    return{
        "name": name,
        "topic": topic,
        "score": score,
        "status": status,
    }


# -------------------------------------------------------
# SECTION 2 — DISPLAY LEARNING REPORT
# -------------------------------------------------------

# This function displays a learningreport.

def display_learning_report(report):

    print()
    print("-" * 50)
    print("Learning Report")
    print("-" * 50)

    print(f"Name    : {report['name']}")
    print(f"Topic   : {report['topic']}")
    print(f"Score   : {report['score']}")
    print(f"Status  : {report['status']}")
    
    print("-" * 50)


# ---------------------------------------------------------
# SECTION 3 — CREATE SAMPLE REPORTS
# ---------------------------------------------------------

# Here we call the function using positional arguments.

report_1 = create_learning_report(
    "Gül",
    "Functions",
    85
)

# Here we call the same function using keyword arguments.

report_2 = create_learning_report(
    name="Gül",
    topic="Python Fundamentals",
    score=45
)


# --------------------------------------------------------
# SECTION 4 — DISPLAY REPORTS
# --------------------------------------------------------


display_learning_report(report_1)
display_learning_report(report_2)



# -----------------------------------------------------------
# SECTION 5 — DEFAULT PARAMETER EXAMPLE
# -----------------------------------------------------------

# The score parameter has a default value of 0.
#
# Because no score is provided here,
# Python automatically uses score=0.

report_3 = create_learning_report(
    name="Gül",
    topic="Future Python Topic"
)

display_learning_report(report_3)




# ------------------------------------------------------------
# SECTION 6 — END OF PROJECT
# ------------------------------------------------------------

print()
print("-" * 80)
print("              END OF TOPİC 15 PRACTICE PROJECT")
print("-" * 80)
print()
