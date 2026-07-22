# Topic 15: Functions — Scope, Parameters and Reusability
# Author: Gül İfdal ALDEMİR
# Date: 22 July 2026
#
# This topic explores how Python functions work with:
# local and global scope, parameters, arguments,
# default parameters, keyword arguments,
# and returning multiple values.
#
# Bu konu Python fonksiyonlarının nasıl çalıştığını inceler:
# local ve global scope, parametreler, argümanlar,
# varsayılan parametreler, keyword arguments
# ve birden fazla değer döndürme.

print()
print("=" * 80)
print("                    TOPİC 15: FUNCTIONS")
print("= * 80")

# ------------------------------------------------------------------------------------
# SECTION 1 - LOCAL SCOBE
# ------------------------------------------------------------------------------------

print()
print("SECTION 1 - LOCAL SCOBE")
print()

# A variable created inside a function has local scope.
# Bir fonksiyonun içinde oluşturulan değişken local scobe'a sahiptir.

def show_local_variable():
    message = "Thia variable exitsts inside the function."
    print(message)

show_local_variable()

# The variable "message" cannot be accesed directly outsie the function.
# "message" değişkenine fonksiyonun dışında doğrudan erişilemez.

# --------------------------------------------------------------------------
# SECTION 2 - GLOBAL SCOBE
# --------------------------------------------------------------------------

print()
print("SECTION 2 - GLOBAL SCOBE")
print()
 
 # A variable created outside a function has global scobe.
 # Fonksiyonun dışında oluşturulan değişken global scobe'a aittir.

course_name = "Python Journey"

def show_course_name():
    print(f"Current course: {course_name}")

show_course_name()
   
# The function can read the global variable.

# --------------------------------------------------
# SECTION 3 — PARAMETERS AND ARGUMENTS
# --------------------------------------------------

print()
print("SECTION 3 — PARAMETERS AND ARGUMENTS")
print()

# "name" and "age" are parameters.

def introduce(name, age):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")

# "Gül" and 21 are arguments passed to the function.

introduce("Gül", 21)

# ------------------------------------
# SECTION 4 — DEFAULT PARAMETERS
# -----------------------------------

print()
print("SECTION 4 — DEFAULT PARAMETERS")
print()

# The default value is used when no argument is provided.
# Argüman verilmediğinde default değer kullanılır.

def greet(name, language="English"):
    if language == "English":
        return f"Hello, {name}!"
    elif language == "Turkish":
        return f"Merhaba, {name}!"
    else:
        return f"Hello, {name}!"
    
print(greet("Gül"))
print(greet("Gül", "Turkish"))

# ---------------------------------
# SECTION 5 — KEYWORD ARGUMENTS
# ---------------------------------

print()
print("SECTION 5 - KEYWORD ARGUMENTS")
print()

# Keyword arguments allow us to specify parameter names directly.

def create_profile(name, role, country):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Country: {country}")


create_profile(
    country="Türkiye",
    role="Python Learner",
    name="Gül"
)

# ---------------------------------------------
# SECTION 6 — RETURNING MULTIPLE VALUES
# BÖLÜM 6 — BİRDEN FAZLA DEĞER DÖNDÜRME
# --------------------------------------------

print()
print("SECTION 6 - RETURNING MULTIPLE VALUES")
print()

# A function can return multiple values.

def calculate_numbers(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


results_sum, result_difference, result_product = calculate_numbers(10,5)

print(f"Sum: {results_sum}")
print(f"Difference: {result_difference}")
print(f"Product: {result_product}")


# ----------------------------------------------------------------
# SECTION 7 — REUSABLE FUNCTIONS
# BÖLÜM 7 — TEKRAR KULLANILABİLİR FONKSİYONLAR
# ----------------------------------------------------------------


print()
print("SECTION 7 — REUSABLE FUNCTIONS")
print()

# Functions help us avoid repeating the same code.
# Fonksiyonlar aynı kodu tekrar tekrar yazmamızı engeller.

def calculate_average(first_grade, second_grade, third_grade):
    total = first_grade + second_grade + third_grade
    average = total / 3
    return average

average_1 = calculate_average(80, 90, 100)
average_2 = calculate_average(60, 70, 75)

print(f"First average: {average_1:.2f}")
print(f"Second average: {average_2:.2f}")



# ---------------------------------------------------------------------------
# SECTION 8 — PRACTICAL EXAMPLE
# BÖLÜM 8 — PRATİK ÖRNEK
# ---------------------------------------------------------------------------

print()
print("SECTION 8 — PRACTICAL EXAMPLE")
print()

# This function combines several concepts from this topic.
# Bu fonksiyon bu konudaki birkaç kavramı birlikte kullanır.

def create_learning_report(name, topic, score=0):
    status = "Completed" if score >= 50 else "Needs Practice"

    return {
        "name": name,
        "topic": topic,
        "score": score,
        "status": status
    }

report = create_learning_report(
    name="Gül",
    topic="Functions",
    score=85
)

print()
print("Learning Report")
print("-" * 40)
print(f"Name: {report['name']}")
print(f"Topic: {report['topic']}")
print(f"Score: {report['score']}")
print(f"Status: {report['status']}")


# ------------------------------------------------------------------
# END OF TOPIC 15
# ------------------------------------------------------------------

print()
print("=" * 80)
print("                       END OF TOPIC 15")
print("=" * 80)
print()

