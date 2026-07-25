# Topic 16: Dictionaries
# Author: Gül İfdal ALDEMİR
# Date: 23 July 2026
#
# This topic explores how Python dictionaries work with:
# key-value pairs, accessing values, adding data,
# updating data, deleting data, dictionary methods,
# and iterating through dictionaries.
#
# Bu konu Python dictionary yapısının nasıl çalıştığını inceler:
# key-value ilişkisi, verilere erişim, veri ekleme,
# veri güncelleme, veri silme, dictionary methodları,
# dictionary üzerinde loop kullanımı,
# nested dictionaries ve functions ile dictionary kullanımı.


print()
print("==========================================================")
print("                    TOPIC 16 - DICTIONARIES")
print("==========================================================")
print()


print("1. CREATING A DICTIONARY")

# A dictionary stores data using key-value pairs.
# Dictionary verileri key-value çiftleri şeklinde saklar.

student = {
    "name": "Gül",
    "age": 21,
    "goal": "AI Engineer"
}

print(student)


print()
print("2. ACCESSING DICTIONARY VALUES")

# We can access a value by using its key.
# Bir value'ya key kullanarak erişebiliriz.

print(student["name"])
print(student["age"])
print(student["goal"])


print()
print("3. ADDING NEW KEY-VALUE PAIRS")

# We can add new key-value pairs to an existing dictionary.
# Var olan bir dictionary'ye yeni key-value çiftleri ekleyebiliriz.

student["university"] = "International Balkan University"
student["language"] = "Python"

print(student)

print(student["university"])
print(student["language"])


print()
print("4. UPDATING DICTIONARY VALUES")

# We can update the value of an existing key.
# Var olan bir key'in value'sunu güncelleyebiliriz.

student["age"] = 22
student["goal"] = "AI Engineer and Developer"

print(student["age"])
print(student["goal"])


print()
print("5. REMOVING DATA")

# The del statement removes a key-value pair from a dictionary.
# In this example, the "language" key and its value are deleted.
#
# del ifadesi bir dictionary içindeki key-value çiftini siler.
# Bu örnekte "language" key'i ve ona bağlı olan value silinir.

del student["language"]

print(student)


print()
print("6. USING POP()")

# The pop() method removes a key-value pair from a dictionary.
# It also returns the value that was removed.
#
# pop() metodu dictionary içinden bir key-value çiftini siler.
# Aynı zamanda silinen value'yu geri döndürür.

removed_goal = student.pop("goal")

print("Removed goal:", removed_goal)
print("Updated student:", student)


print()
print("7. CLEARING A DICTIONARY")

# The clear() method removes all key-value pairs from a dictionary.
# The dictionary itself still exists, but it becomes empty.
#
# clear() metodu dictionary içindeki tüm key-value çiftlerini siler.
# Dictionary'nin kendisi var olmaya devam eder, ancak boş hale gelir.

temporary_data = {
    "name": "Gül",
    "language": "Python"
}

print("Before clear:", temporary_data)

temporary_data.clear()

print("After clear:", temporary_data)


print()
print("8. SAFELY ACCESSING VALUES WITH GET()")

# The get() method accesses a value using its key.
# If the key does not exist, it returns None instead of causing a KeyError.
#
# get() metodu bir key kullanarak value'ya erişmemizi sağlar.
# Eğer key dictionary içinde yoksa KeyError vermek yerine None döndürür.

print("Name:", student.get("name"))

print("Email:", student.get("email"))

# We can also provide a default value if the key does not exist.
# Key dictionary içinde yoksa varsayılan bir değer belirleyebiliriz.

print("Email:", student.get("email", "Email not provided"))


print()
print("9. DICTIONARY METHODS")

# keys() returns all keys in the dictionary.
# keys() dictionary içindeki tüm key'leri döndürür.

print("Keys:", student.keys())


# values() returns all values in the dictionary.
# values() dictionary içindeki tüm value'ları döndürür.

print("Values:", student.values())


# items() returns all key-value pairs.
# items() tüm key-value çiftlerini birlikte döndürür.

print("Items:", student.items())


print()
print("10. USING POPITEM()")

# The popitem() method removes and returns the last inserted key-value pair.
# popitem() metodu dictionary'ye son eklenen key-value çiftini siler ve döndürür.

last_item = student.popitem()

print("Removed item:", last_item)
print("Updated student:", student)


print()
print("11. CHECKING IF A KEY EXISTS")

# The "in" operator checks whether a key exists in a dictionary.
# "in" operatörü bir key'in dictionary içinde olup olmadığını kontrol eder.

if "name" in student:
    print("The name key exists.")


# The "not in" operator checks whether a key does not exist.
# "not in" operatörü bir key'in dictionary içinde olmadığını kontrol eder.

if "email" not in student:
    print("The email key does not exist.")


print()
print("12. LOOPING THROUGH A DICTIONARY")

# We can loop through a dictionary to access its keys.
# Bir dictionary üzerinde loop kullanarak key'lere erişebiliriz.

for key in student:
    print(key)


print()

# We can use values() to loop through only the values.
# values() kullanarak sadece value'lar üzerinde loop yapabiliriz.

for value in student.values():
    print("Value:", value)


print()

# We can use items() to access both keys and values.
# items() kullanarak hem key hem de value'lara erişebiliriz.

for key, value in student.items():
    print(key, ":", value)


print()
print("13. NESTED DICTIONARIES")

# A dictionary can contain another dictionary as a value.
# Bir dictionary'nin value'su başka bir dictionary olabilir.

users = {
    "user_1": {
        "name": "Gül",
        "age": 22
    },
    "user_2": {
        "name": "Erva",
        "age": 17
    }
}

print(users)

# We can access values inside nested dictionaries.
# Nested dictionary içindeki value'lara erişebiliriz.

print(users["user_1"]["name"])
print(users["user_2"]["age"])


print()
print("14. FUNCTIONS AND DICTIONARIES")

# This function creates and returns a dictionary.
# Bu fonksiyon bir dictionary oluşturur ve geri döndürür.

def create_student(name, age, goal):
    student_data = {
        "name": name,
        "age": age,
        "goal": goal
    }

    return student_data


# We call the function and store the returned dictionary.
# Fonksiyonu çağırır ve döndürülen dictionary'yi bir değişkende saklarız.

new_student = create_student(
    "Gül",
    22,
    "AI Engineer"
)

print(new_student)


print()
print("==========================================================")
print("                    END OF TOPIC 16")
print("==========================================================")
print()