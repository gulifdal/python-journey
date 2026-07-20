
# ==========================================
# Topic 13: Dictionary Basics
# Author: Gül İfdal ALDEMİR
# Date: 20 July 2026
#
# Description:
# Learning how to create, update,
# delete and access dictionaries
# in Python.
# ==========================================

print()
print("====================================")
print("         DICTIONARY BASİCS          ")
print("====================================")


student = {
    "first_name": "Gül",
    "middle_name": "İfdal",
    "last_name": "Aldemir",
    "department" : "AI Engineering",
    "university": "International Balkan University"
}

#Dictionary'ye yeni bilgiler ekliyoruz.
student["year"] = 1
student["city"] = "Skopje"
student["country"] = "Türkiye"



# Sınıf bilgisini güncelliyoruz
student["year"] = 2

print()
print("Updated year:")
print(student["year"])

# GPA bilgisini ekliyoruz
student["gpa"] = 3.85

print()
print(student)

# Year bilgisini siliyoruz
del student["year"]

print()
print("Updated student information: ")
print(student)

print(student)

# Dictionary'den belirli bilgilere ulaşıyoruz
print(student["first_name"])
print(student["last_name"])
print(student["department"])
print(student["country"])
print(student["city"])
#print(student["year"])
print(student["gpa"])

#Dictionary'deki tüm key'leri yazdırıyoruz
# "key" değişkeni sırasıyla her anahtarı (key) temsil eder.
# Bu döngü sadece anahatar isimlerini gösterir.

#print()
#print("--------------- Student Information -------------")

#for key in student:
    #print(key, ":", student[key])


# Dictionary'deki hem key hem de value bilgilerini yazdırıyoruz.
# items() metodu her anahtar ve değer çiftini birlikte getirir.
# "key" anahtary temsil eder.
# "value" ise o anahtarın karşılık gelen değerini temsil eder.

#print()
#print("------------- Student Information -------------")

#for key, value in student.items():
    #print(key, ":", value)

#Dictionar bilgilerini daha düzenli bir şekilde yazıyoruz.

#print()
#print("========================= STUDENT CARD ================")

#for key, value in student.items():
    #print(f"{key:<12}: {value}")

    #print("====================================================")



#Student Card'ı dahabokunabilir ve düzenli bir şekilde oluşturuyoruz.
#Burada bilgileri istediğimiz sırayla yazdırıyoruz.
#Bu yöntem gerçek uygulamalrda kullanıcıya daha profesyonel görünür.

print()
print("========================= STUDENT CARD =======================")

print(f"First Name : {student['first_name']}")
print(f"Middle Name : {student['middle_name']}")
print(f"Last Name : {student['last_name']}")
print(f"Department : {student['department']}")
print(f"University : {student['university']}")
print(f"City : {student['city']}")
print(f"Country : {student['country']}")
print(f"GPA : {student['gpa']}")

print("==================================================================")



#Student Card'ı daha okunabilir ve düzenli bir şekilde oluşturuyoruz.
#Burada her başlığı 12 karakterlik bir alana sola yaslıyoruz.
# Böylece tüm ":" işaretleri aynı hizada görünür.

print()
print("========================== STUDENT CARD =============================")

print(f"{'First Name':<12}: {student['first_name']}")
print(f"{'Middle Name':<12}: {student['middle_name']}")
print(f"{'Last Name':<12}: {student['last_name']}")
print(f"{'Department':<12}: {student['department']}")
print(f"{'University':<12}: {student['university']}")
print(f"{'City':<12}: {student['city']}")
print(f"{'Country':<12}: {student['country']}")
print(f"{'GPA':<12}: {student['gpa']}")

print("=====================================================================")

# ==================================
# End of Day 13
#===================================